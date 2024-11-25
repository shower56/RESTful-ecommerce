from factory.django import DjangoModelFactory
from factory import Faker

from apps.products.models import Product


class ProductFactory(DjangoModelFactory):
    name = Faker('pystr')
    description = Faker('pystr')
    price = Faker('pyint')
    discount_rate = Faker('pyfloat')
    coupon_applicable = Faker('pybool')

    class Meta:
        model = Product
