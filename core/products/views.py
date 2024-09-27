from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from core.mixins import ValidatePermissionRequiredMixin
from core.products.forms import *
from core.products.models import Product


# Creación de productos
class ProductCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create_product.html'
    success_url = reverse_lazy('products:product_list')
    permission_required = 'products.add_product'
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
                    messages.success(request, f'Producto creado satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Producto'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['entity'] = 'Creación de Producto'
        return context

# Listado de productos
class ProductListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Product
    template_name = 'product/list_product.html'
    permission_required = 'products.view_product'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                material = list(Product.objects.values(
                    'id',
                    'code_product',
                    'description_product',
                    'presentation_prod',
                    'pharma_form',
                    'product_enabled',
                    'brand_product',
                    'sanitary_license',
                ).order_by('-id'))
                return JsonResponse(material, safe=False)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Productos'
        context['create_url'] = reverse_lazy('products:product_create')
        context['entity'] = 'Productos'
        return context

# Edicion de Producto
class ProductUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'product/create_product.html'
    success_url = reverse_lazy('products:product_list')
    permission_required = 'products.change_product'
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
                    messages.success(request, f'Producto actualizado satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualización de Producto'
        context['list_url'] = self.success_url
        context['entity'] = 'Actualización de Producto'
        context['action'] = 'edit'
        return context

# Detalle de Producto perfil administrador
class ProductDetailView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'product/detail_product.html'
    permission_required = 'products.view_product'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(ProductDetailView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle Producto'
        context['entity'] = 'Detalle Producto'
        # context['stdbatch'] = StandardBatch.objects.filter(product_id=context['object'].id)
        # context['stdbatch_count'] = ProductFormulation.objects.filter(product_id=context['object'].id, std_batch=None).count()
        # context['formprod_count'] = ProductFormulation.objects.filter(product_id=context['object'].id).count()
        # context['packprod_count'] = PackProductFormulation.objects.filter(product_id=context['object'].id).count()
        # context['formulation'] = ProductFormulation.objects.only('mopo_product', 'mopo_porcent', 'std_batch').filter(
        #     product_id=self.kwargs.get('pk'))
        # context['formulation_pack'] = PackProductFormulation.objects.filter(product_id=self.kwargs.get('pk'))
        context['list_url'] = reverse_lazy('products:product_list')
        return context
