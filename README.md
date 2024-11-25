## 프로젝트 개요
Django REST Framework (DRF)를 사용하여 쇼핑몰의 상품 관리 API를 구현합니다. 

API는 기본 상품 리스트 및 카테고리별 진열 기능을 제공하며 상품 상세 페이지에서는 할인율 및 구폰 적요에 따른 가격 변동을 처리하는 비지니스 로직을 구현합니다.

## 구동 버전
python 3.9.11

## 서버 구동을 위한 명령어 순서

> git clone https://github.com/shower56/RESTful-ecommerce.git

> cd RESTful-ecommerce/

> pip install -r ./requirements/base.txt

> cd ecommerce/

> ./manage.py runserver

> browser <http://127.0.0.1:8000/v1/doc/>


## 테스트 커버리지 확인하기

> pytest --cov . --cov-report=html
 
> browser htmlcov/index.html  