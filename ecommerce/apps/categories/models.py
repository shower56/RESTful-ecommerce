from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models.base import TimeStampedMixin


class Category(TimeStampedMixin):
    name = models.CharField(_("category"), max_length=100, null=False, blank=False)
