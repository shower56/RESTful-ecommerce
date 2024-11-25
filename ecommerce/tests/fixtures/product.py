import random

import pytest

from apps.categories.models import Category
from tests.factories.product import ProductFactory
from tests.fixtures.category import categories


@pytest.fixture()
def products():
    c = Category.objects.all()

    for _ in range(100):
        category_idx = random.randrange(0, 10)
        ProductFactory(category=c[category_idx])
