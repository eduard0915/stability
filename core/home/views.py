from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BPMPro Estabilidades'
        return context

class SinpermisosView(TemplateView):
    # template_name = 'sinpermisos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sin Permisos de Acceso'
        return context
