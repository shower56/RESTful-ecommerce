from rest_framework import mixins

from apis.v1.categories.serializers import CategorySerializer
from apps.categories.models import Category
from core.viewsets.base import CustomViewSet


class CategoryViewSet(mixins.ListModelMixin, CustomViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
