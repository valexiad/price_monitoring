from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
import uuid

class TrackItemHeader(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TrackItemComponents(models.Model):
    class SiteTypes(models.TextChoices):
        SKROUTZ = 'SK', _('SKROUTZ')
        BANGGOOD = 'BG', _('BANGGOOD')
        LEROY = 'LR', _('Leroy Merlin')
        PRAKTIKER = 'PR', _('Praktiker')


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    header = models.ForeignKey(TrackItemHeader, on_delete=models.CASCADE)
    url = models.CharField(max_length=150)
    site_type = models.CharField(
        max_length=2,
        choices=SiteTypes.choices,
        default=SiteTypes.SKROUTZ,
    )
     


