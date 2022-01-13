from django.forms import *

from core.products.models import *


# Creación de producto
class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Product
        fields = [
            'code_product',
            'description_product',
            'pharma_form',
            'presentation_prod',
            'brand_product',
            'sanitary_license',
        ]
        widgets = {
            'code_product': TextInput(attrs={'class': 'form-control', 'required': True}),
            'description_product': TextInput(attrs={'class': 'form-control', 'required': True}),
            'pharma_form': Select(attrs={'class': 'form-control', 'required': True}),
            'presentation_prod': TextInput(attrs={'class': 'form-control', 'required': True}),
            'brand_product': TextInput(attrs={'class': 'form-control'}),
            'sanitary_license': TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                data = form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

# Edición de producto
class ProductUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Product
        fields = [
            'code_product',
            'description_product',
            'pharma_form',
            'presentation_prod',
            'brand_product',
            'sanitary_license',
            'product_enabled',
        ]
        widgets = {
            'code_product': TextInput(attrs={'class': 'form-control', 'required': True}),
            'description_product': TextInput(attrs={'class': 'form-control', 'required': True}),
            'pharma_form': Select(attrs={'class': 'form-control', 'required': True}),
            'presentation_prod': TextInput(attrs={'class': 'form-control', 'required': True}),
            'brand_product': TextInput(attrs={'class': 'form-control'}),
            'sanitary_license': TextInput(attrs={'class': 'form-control'}),
            'product_enabled': NullBooleanSelect(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                data = form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
