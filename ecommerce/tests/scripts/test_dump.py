import pytest

from apps.categories.models import Category
from apps.coupons.models import Coupon
from apps.products.models import Product
from scripts.dump import run


@pytest.mark.django_db
class TestCategoryAPI:

    def test_dump(self):
        """
        ecommerce 구동을 위해서 사전 dump 데이터 생성

        :param url: 카테고리 API 접근 url
        :param client_user_anonymous: 익명 유저의 Client instance
        :param categories: Factory로서 테스트전에 미리 생성한 테스트용 카테고리 데이터
        """

        run()

        categories = Category.objects.all()
        assert 15 == categories.count()
        for category in categories:
            assert category.id
            assert category.created
            assert category.modified
            assert category.name

        coupons = Coupon.objects.all()
        assert 20 == coupons.count()
        for coupon in coupons:
            assert coupon.id
            assert coupon.created
            assert coupon.modified
            assert coupon.code
            assert coupon.discount_rate

        products = Product.objects.all()
        assert 500 == products.count()
        for product in products:
            assert product.id
            assert product.created
            assert product.modified
            assert product.name
            assert product.description
            assert hasattr(product, 'price')
            assert product.category
            assert product.category.id
            assert product.category.name
            assert hasattr(product, 'discount_rate')
            assert hasattr(product, 'coupon_applicable')
