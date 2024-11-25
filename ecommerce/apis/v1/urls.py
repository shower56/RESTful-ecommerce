from django.urls import path
from rest_framework.routers import DefaultRouter

from apis.v1.categories.views import CategoryViewSet
from apis.v1.products.views import ProductViewSet

from drf_spectacular.views import SpectacularSwaggerView, SpectacularJSONAPIView

app_name = 'api'

router = DefaultRouter()

router.register(r'category', CategoryViewSet, 'ecommerce-category')
router.register(r'product', ProductViewSet, 'ecommerce-product')

urlpatterns = router.urls

# 스퀘거 API 문서 페이지는 개발환경에서만 load 가능하도록 environment 별 관리가 필요하겠습니다.
urlpatterns += [
    path("schema/", SpectacularJSONAPIView.as_view(), name="schema"),
    path("doc/", SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger-ui'),
]
