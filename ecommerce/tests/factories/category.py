from factory.django import DjangoModelFactory
from factory import Faker

from apps.categories.models import Category


class CategoryFactory(DjangoModelFactory):
    name = Faker('pystr')

    class Meta:
        model = Category
