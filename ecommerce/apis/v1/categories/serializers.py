from apps.categories.models import Category
from core.serializers.base import CustomModelSerializer


class CategorySerializer(CustomModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')
