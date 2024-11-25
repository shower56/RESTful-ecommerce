from rest_framework import serializers

from apis.v1.categories.serializers import CategorySerializer
from apps.coupons.models import Coupon
from apps.products.models import Product
from core.serializers.base import CustomModelSerializer


class ProductListSerializer(CustomModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category', 'discount_rate', 'coupon_applicable')
        no_update_fields = ('id',)


class ProductRetrieveSerializer(ProductListSerializer):
    discounted_price = serializers.SerializerMethodField(label="상품 할인가")
    coupon_applied_prices = serializers.SerializerMethodField(label="쿠폰 적용가")

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'discounted_price', 'category', 'discount_rate', 'coupon_applicable', 'coupon_applied_prices')
        no_update_fields = ('id',)

    def get_discounted_price(self, obj):
        price = obj.price
        discount_rate = obj.discount_rate

        try:
            discounted_price = int(price * discount_rate)
        except Exception:
            discounted_price = 0
        return price - discounted_price

    def get_coupon_applied_prices(self, obj):
        """
        상품에 쿠폰 적용가능 여부 coupon_applicable의 필드의 경우 상품에 대해 쿠폰을 적용할 수 있는 Flag이며,
        상품에 적용할 쿠폰과의 관계 정의가 필요할 것으로 보입니다.
        대게 상품에 적용된 쿠폰적용가를 표시할 경우
            1. User가 보유한 쿠폰을 적용한 가격
            2. 해당 상품에 받을수 있는 쿠폰을 적용한 가격
        위 같이 상품과 쿠폰간의 관계를 정의할만한 주제가 필요합니다.

        해당 과제에선 상품과 쿠폰간의 정의가 모호하여
        우선, 현재 모든 쿠폰 코드별로 각 상품에 적용가능한 쿠폰가를 명시하도록 하겠습니다.
        """

        if not obj.coupon_applicable:
            return []

        coupons = Coupon.objects.all()
        discounted_price = self.get_discounted_price(obj)

        coupon_applied_prices = []

        for coupon in coupons:
            try:
                coupon_applied_price = int(discounted_price * coupon.discount_rate)
            except Exception:
                coupon_applied_price = 0
            coupon_applied_prices.append({
                'code': coupon.code,
                'discount_rate': coupon.discount_rate,
                'coupon_applied_price': (discounted_price - coupon_applied_price),
            })

        return coupon_applied_prices
