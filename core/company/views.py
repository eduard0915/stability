from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, ListView

from core.company.forms import CompanyForms
from core.company.models import Company
from core.mixins import ValidatePermissionRequiredMixin


class CompanyCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForms
    template_name = 'create_company.html'
    success_url = reverse_lazy('company:company_list')
    permission_required = 'company.add_company'

    def dispatch(self, request, *args, **kwargs):
        try:
            Company.objects.get(id=1)
            return redirect('company:company_list')
        except ObjectDoesNotExist:
            pass
        return super(CompanyCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    data = form.save()
                    messages.success(request, f'Compañia creada satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Perfil Compañia'
        context['entity'] = 'Perfil Compañia'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('company:company_list')
        return context


class CompanyUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForms
    template_name = 'create_company.html'
    success_url = reverse_lazy('company:company_list')
    permission_required = 'company.change_company'
    url_redirect = success_url

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
                    data = form.save()
                    messages.success(request, f'La compañia se ha editado satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha editado los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Compañia'
        context['entity'] = 'Editar Información Compañía'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('company:company_list')
        return context


class CompanyListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Company
    template_name = 'list_company.html'
    permission_required = 'company.view_company'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                empresa = list(Company.objects.values(
                    'id', 'companyName', 'companyNit', 'companyAddress', 'companyCity',
                ).filter(id=1))
                return JsonResponse(empresa, safe=False)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Perfil Compañia'
        context['entity'] = 'Perfil Compañia'
        context['create_url'] = reverse_lazy('company:company_create')
        return context
