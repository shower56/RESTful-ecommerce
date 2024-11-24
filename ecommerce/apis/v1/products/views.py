from rest_framework import mixins
from rest_framework.settings import api_settings

from apis.v1.products.filter import ProductFilterBackend
from apis.v1.products.serializers import ProductListSerializer, ProductRetrieveSerializer
from apps.products.models import Product
from core.viewsets.base import CustomViewSet
from core.viewsets.pagination import CustomPagination


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, CustomViewSet):

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
        serializer_class = {
            "list": ProductListSerializer,
            "retrieve": ProductRetrieveSerializer,
        }
        return serializer_class.get(self.action, ProductListSerializer)
