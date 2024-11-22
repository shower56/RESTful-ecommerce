from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models.base import TimeStampedMixin


class Product(TimeStampedMixin):
    name = models.CharField(_("product name"), max_length=24, null=False, blank=False)
    description = models.TextField(_("product description"))
    price = models.IntegerField(_("product price"))
    category = models.ForeignKey("categories.Category", related_name="products", db_constraint=False, on_delete=models.DO_NOTHING)
    discount_rate = models.FloatField(_("discount_rate"))
    coupon_applicable = models.BooleanField(_("product coupon applicable"), default=False)

    class Meta:

        indexes = [
            models.Index(fields=['name'], name="idx_name"),
            models.Index(fields=['price'], name="idx_price"),
            models.Index(fields=['category'], name="idx_category")
        ]
