from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid

class TrackItemHeader(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     super().save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

# @receiver(pre_save, sender=TrackItemHeader)
# def create_slug(sender, instance, *args, **kwargs):
#    test = 1


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
     


