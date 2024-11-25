from django.urls import reverse
from rest_framework import status
from tests.fixtures.base import *
from tests.fixtures.category import categories


@pytest.mark.urls(urls="apis.v1.urls")
@pytest.mark.django_db
class TestCategoryAPI:
    category_basename = "ecommerce-category-list"

    @pytest.mark.parametrize("url", [category_basename])
    def test_category_list_by_anonymous(self, url, client_user_anonymous, categories):
        """
        Given : 카테고리 목록 조회
        When : 익명 사용자
        Then : 카테고리 목록 데이터 조회가능

        `ecommerce-category-list` API의 permission class 가 AllowAny로 되었음을 테스트
        :param url: 카테고리 API 접근 url
        :param client_user_anonymous: 익명 유저의 Client instance
        :param categories: Factory로서 테스트전에 미리 생성한 테스트용 카테고리 데이터
        """
        path = reverse(viewname=url)
        response = client_user_anonymous.get(path=path)
        assert response.status_code == status.HTTP_200_OK
        assert 5 == len(response.json()['results'])

        for row in response.json()['results']:
            assert 'id' in row
            assert 'name' in row
