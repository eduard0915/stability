from django.forms import ModelForm, TextInput, Select

from core.condition.models import Condition

SELECT = [(False, 'No'), (True, 'Si')]

ZONE = [('Zona I', 'Zona I'), ('Zona II', 'Zona II'), ('Zona III', 'Zona III'), ('Zona IV', 'Zona IV')]


# Creación de Condition
class ConditionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Condition
        fields = ['zone', 'temperature_inf', 'temperature_sup', 'humidity_inf', 'humidity_sup']
        widgets = {
            'zone': Select(attrs={'class': 'form-control', 'required': True}, choices=ZONE),
            'temperature_inf': TextInput(attrs={'class': 'form-control', 'required': True}),
            'temperature_sup': TextInput(attrs={'class': 'form-control', 'required': True}),
            'humidity_inf': TextInput(attrs={'class': 'form-control', 'required': True}),
            'humidity_sup': TextInput(attrs={'class': 'form-control', 'required': True}),
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
