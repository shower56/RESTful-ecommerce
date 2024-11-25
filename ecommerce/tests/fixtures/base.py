import pytest

from rest_framework.test import APIClient


@pytest.fixture()
def client_user_anonymous():
    """
    일반 유저
    """
    client = APIClient()
    return client
