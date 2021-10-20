from django.forms import *

from core.company.models import Company


class CompanyForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Company
        fields = 'companyName', 'companyNit', 'companyAddress', 'companyLogo', 'companyCity'
        widgets = {
            'companyLogo': FileInput(attrs={'class': 'form-control-file'}),
            'companyName': TextInput(attrs={'class': 'form-control', 'required': True}),
            'companyNit': TextInput(attrs={'class': 'form-control', 'required': True}),
            'companyAddress': TextInput(attrs={'class': 'form-control', 'required': True}),
            'companyCity': TextInput(attrs={'class': 'form-control', 'required': True}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
