from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict


class User(AbstractUser):
    cedula = models.CharField(max_length=15, null=True, blank=True, unique=False, verbose_name='Cédula')
    cargo = models.CharField(max_length=50, null=True, blank=True, verbose_name='Cargo')
    cellphone = models.CharField(max_length=10, null=True, blank=True, verbose_name='N° Celular')

    def __str__(self):
        return f'{self.get_full_name()}, {self.cargo}'

    def tojson(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d %H:%M')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['full_name'] = self.get_full_name()
        # item['is_active'] = self.is_active_display()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item
