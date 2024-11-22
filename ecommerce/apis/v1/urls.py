from django.conf.urls import url

from apis.v1.categories.views import CategoryViewSet
from apis.v1.products.views import ProductViewSet

from drf_spectacular.views import SpectacularSwaggerView, SpectacularJSONAPIView

urlpatterns = [
    url(r'^product/', ProductViewSet.as_view({'get': 'list'}), name='product'),
    url(r'^category/', CategoryViewSet.as_view({'get': 'list'}), name='category'),
]

# 스퀘거 API 문서 페이지는 개발환경에서만 load 가능하도록 environment 별 관리가 필요하겠습니다.
urlpatterns += [
    url("schema/", SpectacularJSONAPIView.as_view(), name="schema"),
    url("^doc/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
