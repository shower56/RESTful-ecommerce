from urllib.parse import urlencode

from django.urls import reverse
from rest_framework import status

from apps.categories.models import Category
from apps.products.models import Product
from tests.fixtures.base import *
from tests.fixtures.product import products
from tests.fixtures.category import categories


@pytest.mark.urls(urls="apis.v1.urls")
@pytest.mark.django_db
class TestProductAPI:
    product_basename = "ecommerce-product-list"
    product_detail = "ecommerce-product-detail"

    @pytest.mark.parametrize("url", [product_basename])
    def test_product_list_by_anonymous(self, url, client_user_anonymous, categories, products):
        """
        `ecommerce-product-list` API의 permission class 가 AllowAny로 되었음을 테스트

        Given : 상품 목록 조회
        When : 익명 사용자
        Then : 상품 조회

        :param url: tkdvna API 접근 url
        :param client_user_anonymous: 익명 유저의 Client instance
        :param products: Factory로서 테스트전에 미리 생성한 테스트용 상품 데이터
        """
        path = reverse(viewname=url)
        response = client_user_anonymous.get(path=path)
        assert response.status_code == status.HTTP_200_OK
        assert 5 == len(response.json()['results'])

        for row in response.json()['results']:
            assert 'id' in row
            assert 'name' in row
            assert 'description' in row
            assert 'price' in row
            assert 'category' in row
            assert 'id' in row['category']
            assert 'name' in row['category']
            assert 'discount_rate' in row
            assert 'coupon_applicable' in row


    @pytest.mark.parametrize("url", [product_basename])
    def test_product_list_with_query_string_by_anonymous(self, url, client_user_anonymous, categories, products):
        """
        `ecommerce-product-list` API의 permission class 가 AllowAny로 되었음을 테스트
        카테고리 별로 상품 조회 테스트

        Given : 상품 목록 조회
        When : 익명 사용자, 카테고리 별 조회
        Then : 해당 카테고리에 포함된 상품 조회

        :param url: tkdvna API 접근 url
        :param client_user_anonymous: 익명 유저의 Client instance
        :param products: Factory로서 테스트전에 미리 생성한 테스트용 상품 데이터
        """
        category = Category.objects.last()
        query_string = {"category": category.id}

        path = f"{reverse(viewname=url)}?{urlencode(query_string)}"
        response = client_user_anonymous.get(path=path)
        assert response.status_code == status.HTTP_200_OK
        assert 5 == len(response.json()['results'])

        for row in response.json()['results']:
            assert 'id' in row
            assert 'name' in row
            assert 'description' in row
            assert 'price' in row
            assert 'category' in row
            assert 'id' in row['category']
            assert row['category']['id'] == category.id
            assert 'name' in row['category']
            assert 'discount_rate' in row
            assert 'coupon_applicable' in row


    @pytest.mark.parametrize("url", [product_basename])
    def test_product_list_with_not_exist_query_string_by_anonymous(self, url, client_user_anonymous, categories, products):
        """
        `ecommerce-product-list` API의 permission class 가 AllowAny로 되었음을 테스트
        카테고리 별로 상품 조회 테스트

        Given : 상품 목록 조회
        When : 익명 사용자, 존재 하지 않는 카테고리 id
        Then : 모든 카데고리의 상품 목록 조회

        :param url: tkdvna API 접근 url
        :param client_user_anonymous: 익명 유저의 Client instance
        :param products: Factory로서 테스트전에 미리 생성한 테스트용 상품 데이터
        """
        category = Category.objects.last()
        query_string = {"category": category.id + 100}

        path = f"{reverse(viewname=url)}?{urlencode(query_string)}"
        response = client_user_anonymous.get(path=path)
        assert response.status_code == status.HTTP_200_OK
        assert 5 == len(response.json()['results'])

        for row in response.json()['results']:
            assert 'id' in row
            assert 'name' in row
            assert 'description' in row
            assert 'price' in row
            assert 'category' in row
            assert 'id' in row['category']
            assert 'name' in row['category']
            assert 'discount_rate' in row
            assert 'coupon_applicable' in row


    @pytest.mark.parametrize("url", [product_basename])
    def test_product_list_with_invalid_query_string_by_anonymous(self, url, client_user_anonymous, categories, products):
        """
        `ecommerce-product-list` API의 permission class 가 AllowAny로 되었음을 테스트
        카테고리 별로 상품 조회 테스트

        Given : 상품 목록 조회
        When : 익명 사용자, 조회할 수 없는 카테고리 ID
        Then : 모든 카데고리의 상품 목록 조회

        :param url: tkdvna API 접근 url
        :param client_user_anonymous: 익명 유저의 Client instance
        :param products: Factory로서 테스트전에 미리 생성한 테스트용 상품 데이터
        """
        category = Category.objects.last()
        query_string = {"category": f"{category.id}_abc"}

        path = f"{reverse(viewname=url)}?{urlencode(query_string)}"
        response = client_user_anonymous.get(path=path)
        assert response.status_code == status.HTTP_200_OK
        assert 5 == len(response.json()['results'])

        for row in response.json()['results']:
            assert 'id' in row
            assert 'name' in row
            assert 'description' in row
            assert 'price' in row
            assert 'category' in row
            assert 'id' in row['category']
            assert 'name' in row['category']
            assert 'discount_rate' in row
            assert 'coupon_applicable' in row


    @pytest.mark.parametrize("url", [product_detail])
    def test_product_detail_by_anonymous(self, url, client_user_anonymous, categories, products):
        """
        `ecommerce-product-list` API의 permission class 가 AllowAny로 되었음을 테스트

        Given : 상품 상세 조회
        When : 익명 사용자
        Then : 상품 상세 조회

        :param url: tkdvna API 접근 url
        :param client_user_anonymous: 익명 유저의 Client instance
        :param products: Factory로서 테스트전에 미리 생성한 테스트용 상품 데이터
        """
        product = Product.objects.last()
        kwargs = {"pk": product.id}
        path = reverse(viewname=url, kwargs=kwargs)
        response = client_user_anonymous.get(path=path)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert 'id' in data
        assert 'name' in data
        assert 'price' in data
        assert 'discounted_price' in data
        assert 'category' in data
        assert 'id' in data['category']
        assert 'name' in data['category']
        assert 'discount_rate' in data
        assert 'coupon_applicable' in data
        if data['coupon_applicable']:
            for coupon in data['coupon_applied_prices']:
                assert 'code' in coupon
                assert 'discount_rate' in coupon
                assert 'coupon_applied_pirce' in coupon


