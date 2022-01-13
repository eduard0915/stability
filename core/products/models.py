from crum import get_current_user
from djchoices import DjangoChoices, ChoiceItem

from django.db import models
from core.models import BaseModel


# Formas Farmaceuticas
class FormPharma(DjangoChoices):
    tablet = ChoiceItem('Tableta', 'Tableta')
    capsule = ChoiceItem('Capsula', 'Capsula')
    granulate = ChoiceItem('Granulado', 'Granulado')
    supository = ChoiceItem('Supositorio', 'Supositorio')
    polvo = ChoiceItem('Polvo para Reconstituir', 'Polvo para Reconstituir')
    crema = ChoiceItem('Crema', 'Crema')
    unguento = ChoiceItem('Unguento', 'Unguento')
    paste = ChoiceItem('Pasta', 'Pasta')
    emulsion = ChoiceItem('Emulsión', 'Emulsión')
    gel = ChoiceItem('Gel', 'Gel')
    syrupe = ChoiceItem('Jarabe', 'Jarabe')
    suspention = ChoiceItem('Suspensión', 'Suspensión')
    elix = ChoiceItem('Elixir', 'Elixir')
    solution = ChoiceItem('Solución', 'Solución')


# Productos
class Product(BaseModel):
    code_product = models.CharField(max_length=15, unique=True, verbose_name='Código')
    description_product = models.CharField(max_length=80, verbose_name='Principio y Concentración')
    pharma_form = models.CharField(max_length=80, verbose_name='Forma Farmacéutica', choices=FormPharma.choices)
    presentation_prod = models.CharField(max_length=80, verbose_name='Presentación')
    brand_product = models.CharField(max_length=80, verbose_name='Nombre Comercial')
    sanitary_license = models.CharField(max_length=80, verbose_name='Registro Sanitario')
    product_enabled = models.BooleanField(default=True, verbose_name='Habilitado')

    def __str__(self):
        return f'{self.code_product} {self.description_product} {self.pharma_form} - {self.brand_product}'

    class Meta:
        db_table = 'Product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        self.description_product = self.description_product.capitalize()
        self.presentation_prod = self.presentation_prod.capitalize()
        self.brand_product = self.brand_product.capitalize()
        self.code_product = self.code_product.upper()
        self.sanitary_license = self.sanitary_license.upper()
        return super(Product, self).save(*args, **kwargs)
