from django.db import models

from config.settings import MEDIA_URL, STATIC_URL


class Company(models.Model):
    companyName = models.CharField(default='Nombre compañia', max_length=120, verbose_name='Nombre Compañia', null=True)
    companyLogo = models.ImageField(upload_to='company', null=True, blank=True, verbose_name='Logo',
                                    help_text='jpg, png 2MB Max.')
    companyNit = models.CharField(default='0000000000-0', max_length=20, verbose_name='NIT', null=False)
    companyAddress = models.CharField(default='Direccion', max_length=60, verbose_name='Dirección',
                                      null=True, blank=True)
    companyCity = models.CharField(max_length=60, verbose_name='Ciudad', null=True, blank=True)

    def __str__(self):
        return self.companyName

    def get_logo(self):
        if self.companyLogo:
            return '{}{}'.format(MEDIA_URL, self.companyLogo)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        db_table = 'Company'

