import pytest

from tests.factories.category import CategoryFactory


@pytest.fixture()
def categories():
    CategoryFactory.create_batch(size=10)
