import uuid

from crum import get_current_user
from django.db import models

from core.models import BaseModel


# Condiciones Ambientales
class Condition(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    zone = models.CharField(max_length=15, verbose_name='Zona')
    temperature_inf = models.PositiveSmallIntegerField(verbose_name='Temperatura Inferior')
    temperature_sup = models.PositiveSmallIntegerField(verbose_name='Temperatura Superior')
    humidity_inf = models.PositiveSmallIntegerField(verbose_name='Húmedad Inferior', null=True, blank=True)
    humidity_sup = models.PositiveSmallIntegerField(verbose_name='Húmedad Superior', null=True, blank=True)
    enable = models.BooleanField(verbose_name='', default=True)

    def __str__(self):
        return str(self.zone)

    class Meta:
        db_table = 'Condition'
        verbose_name = 'Condition'
        verbose_name_plural = 'Conditions'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs):
        user = get_current_user()
        if user:
            if not self.user_creation:
                self.user_creation = user
            else:
                self.user_updated = user
        return super(Condition, self).save(*args, **kwargs)
