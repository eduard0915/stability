from django.contrib import admin

from core.products.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('code_product', 'description_product', 'pharma_form', 'presentation_prod', 'brand_product', 'sanitary_license', 'product_enabled')


# Register your models here.
admin.site.register(Product, ProductAdmin)

