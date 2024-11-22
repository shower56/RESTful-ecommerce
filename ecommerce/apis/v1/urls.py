from django.conf.urls import url

from apis.v1.categories.views import CategoryViewSet
from apis.v1.products.views import ProductViewSet

urlpatterns = [
    url(r'^product/', ProductViewSet.as_view({'get': 'list'}), name='product'),
    url(r'^category/', CategoryViewSet.as_view({'get': 'list'}), name='category'),
]
