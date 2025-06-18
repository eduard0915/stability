from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView

from core.condition.forms import *
from core.condition.models import Condition
from core.mixins import ValidatePermissionRequiredMixin


# Creación de Proveedores
class ConditionCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Condition
    form_class = ConditionForm
    template_name = 'create_condition.html'
    success_url = reverse_lazy('condition:list_condition')
    permission_required = 'condition.add_condition'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                    messages.success(request, f'Condicion Ambiental creada satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Condicion Ambiental'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['div'] = '6'
        context['icon'] = 'thermostat'
        context['entity'] = 'Creación de Condicion Ambiental'
        return context


# Listado de Condiciones Ambientales
class ConditionListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Condition
    template_name = 'list_condition.html'
    permission_required = 'materials.view_suppliermaterial'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                material = list(Condition.objects.values(
                    'id', 'zone', 'temperature_inf', 'temperature_sup', 'humidity_inf', 'humidity_sup'
                ).order_by('zone'))
                return JsonResponse(material, safe=False)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Condiciones Ambientales para Estudios'
        context['create_url'] = reverse_lazy('condition:create_condition')
        context['entity'] = 'Condiciones Ambientales para Estudios de Estabilidad'
        context['div'] = '6'
        return context


# Edición de Condiciones Ambientales
class ConditionUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Condition
    form_class = ConditionForm
    template_name = 'create_condition.html'
    success_url = reverse_lazy('materials:supplier_list')
    permission_required = 'materials.change_suppliermaterial'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                    messages.success(request, f'Condicion Ambiental actualizado satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualización de Condicion Ambiental'
        context['list_url'] = self.success_url
        context['entity'] = 'Actualización de Condicion Ambiental'
        context['action'] = 'edit'
        context['icon'] = 'thermostat'
        context['div'] = '6'
        return context
