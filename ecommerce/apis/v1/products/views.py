from rest_framework import mixins

from apps.products.models import Product
from core.viewsets.base import CustomViewSet


class ProductViewSet(mixins.ListModelMixin, CustomViewSet):

    queryset = Product
