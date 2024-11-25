from drf_spectacular.utils import extend_schema_view
from rest_framework import mixins
from rest_framework.settings import api_settings

from apis.v1.products.filter import ProductFilterBackend
from apis.v1.products.serializers import ProductListSerializer, ProductRetrieveSerializer
from apis.v1.products.swaggers import PRODUCT_LIST, PRODUCT_RETRIEVE
from apps.products.models import Product
from core.viewsets.base import CustomViewSet
from core.viewsets.pagination import CustomPagination


@extend_schema_view(list=PRODUCT_LIST, retrieve=PRODUCT_RETRIEVE)
class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, CustomViewSet):
    """
    요구사항

    - 상품 리스트 및 카테고리 진열
    사용자는 전체 상품 리스트를 조회할 수 있어야 하며 카테고리별로 상품을 필터링할 수 있어야 합니다.
    각 상품은 다음과 같은 정보를 포함합니다:상품 이름, 설명, 가격, 카테고리, 할인율(있을 경우), 쿠폰 적용 가능 여부

    - 상품 상세 정보
    사용자는 특정 상품의 상세 정보를 조회할 수 있습니다.
    상세 페이지에서는 할인율을 적용한 할인 가격을 함께 반환해야 합니다.
    (예: 원래 가격과 할인 가격을 모두 표시)상품에 쿠폰이 적용된 경우 쿠폰 할인율을 적용한 최종 가격도 표시해야 합니다.

    - 쿠폰 적용
    상품에 적용할 수 있는 쿠폰 목록을 제공하며 쿠폰이 적용된 상품은 할인이 추가되어 최종 가격을 계산해야 합니다.
    비즈니스 로직 :
        - 할인율은 상품별로 다를 수 있습니다.
        - 쿠폰이 적용되면 상품의 할인 가격에 추가로 쿠폰 할인이 적용되어 최종 가격이 결정됩니다.
    """

    # 사품 기본 쿼리셋 세팅
    queryset = Product.objects.all()
    # drf에서 제공하는 기본 퍼미션 AllowAny로 세팅
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    # 기본 데이터 시리얼라이저 클래스 세팅
    serializer_class = ProductListSerializer
    # List Mixin에서 사용될 기본 페이지네이션 클래스 세팅
    pagination_class = CustomPagination
    # List 조회시 Query string으로 카테고리별 필터링 세팅
    filter_backends = [ProductFilterBackend]

    def get_serializer_class(self):
        """
        API의 action에 따라 필요한 serializer class를 할당합니다.
        """
        serializer_class = {
            "list": ProductListSerializer,
            "retrieve": ProductRetrieveSerializer,
        }
        return serializer_class.get(self.action, ProductListSerializer)
