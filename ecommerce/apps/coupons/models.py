from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models.base import TimeStampedMixin


class Coupon(TimeStampedMixin):
    code = models.CharField(_("category"), max_length=24, null=False, blank=False)
    discount_rate = models.FloatField(_("discount_rate"))
