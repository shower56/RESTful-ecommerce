from rest_framework.filters import BaseFilterBackend

from apps.categories.models import Category


class ProductFilterBackend(BaseFilterBackend):
    """
    상품 API의 List Mixin에서 사용될 필터 클래스
    url에 category가 포함되어 있다면 해당 카테고리로 필터링
    """
    def filter_queryset(self, request, queryset, view):
        category_id = request.query_params.get('category')
        if not category_id or not category_id.isdigit():
            return queryset

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return queryset

        return queryset.filter(category=category)
