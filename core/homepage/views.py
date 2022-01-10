from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BPMPro Estabilidades'
        return context


class NotPermsView(TemplateView):
    template_name = 'notperms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sin Permisos de Acceso'
        return context
