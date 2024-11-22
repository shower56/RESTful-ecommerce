from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class AbstractPrimaryModel(models.Model):
    """
    모든 Model의 base model로 id값을 갖는다.
    """
    id = models.BigAutoField(_('id'), primary_key=True)

    class Meta:
        abstract = True


class TimeStampedMixin(AbstractPrimaryModel):
    """
    데이터의 생싱일과 수정일 표시를 위하여 필요한 데이터 구조에 상속받아 사용한다.
    데이터 row 최초 생성시에는 created, modified 를 현재값으로 세팅하며, 추후 변경된 모든 건은 modified만 반경된다.

    만약 modified가 필요없거나 created, modified가 모두 필요없을경우 AbstractPrimaryModel를 상속받아 모델을 구성한다.
    """
    created = models.DateTimeField(_('created date'), blank=True, editable=False)
    modified = models.DateTimeField(_('modified date'), blank=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        now = timezone.now()

        if not self.id:
            self.created = now
        self.modified = now

        update_fields = kwargs.get('update_fields', None)
        if isinstance(update_fields, list):
            update_fields.append('modified')

        super().save(*args, **kwargs)
