from rest_framework import mixins
from rest_framework.settings import api_settings

from apis.v1.categories.serializers import CategorySerializer
from apps.categories.models import Category
from core.viewsets.base import CustomViewSet
from core.viewsets.pagination import CustomPagination


class CategoryViewSet(mixins.ListModelMixin, CustomViewSet):

    # 카테고리 기본 쿼리셋 세팅
    queryset = Category.objects.all()
    # drf에서 제공하는 기본 퍼미션 AllowAny로 세팅
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    # 기본 데이터 시리얼라이저 클래스 세팅
    serializer_class = CategorySerializer
    # List Mixin에서 사용될 기본 페이지네이션 클래스 세팅
    pagination_class = CustomPagination
