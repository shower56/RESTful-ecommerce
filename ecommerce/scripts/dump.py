import random

from django.utils import timezone
from faker import Faker
import faker_commerce

from apps.coupons.models import Coupon
from apps.categories.models import Category
from apps.products.models import Product


class Dump:
    def __init__(self):
        self.fake = Faker("ko_KR")
        self.fake.add_provider(faker_commerce.Provider)
        self.now = timezone.now()

    def dump(self):
        self.create_category_dump()
        self.create_product_dump()
        self.create_coupon_dump()

    def create_coupon_dump(self):
        coupons = []
        coupon_codes = [self.fake.unique.word().upper() for i in range(20)]
        for code in coupon_codes:
            coupons.append(
                Coupon(
                    created=self.now,
                    modified=self.now,
                    code=code,
                    discount_rate=round(random.random(), 2),
                )
            )
        Coupon.objects.bulk_create(coupons)

    def create_category_dump(self):
        categories = []
        category_names = [self.fake.unique.ecommerce_category() for i in range(15)]
        for name in category_names:
            categories.append(
                Category(
                    created=self.now,
                    modified=self.now,
                    name=name,
                )
            )
        Category.objects.bulk_create(categories)

    def create_product_dump(self):
        categories = Category.objects.all()
        categories_size = len(categories)
        products = []
        product_names = [self.fake.unique.ecommerce_name() for i in range(500)]

        for idx, name in enumerate(product_names):
            category_id = idx % categories_size
            products.append(
                Product(
                    created=self.now,
                    modified=self.now,
                    name=name,
                    description=self.fake.text(),
                    price=self.fake.ecommerce_price() % 1000 * 100,
                    category=categories[category_id],
                    discount_rate=round(random.random(), 2),
                    coupon_applicable=self.fake.boolean(),
                )
            )

        Product.objects.bulk_create(products)


def run():
    Dump().dump()
    print("DONE")

