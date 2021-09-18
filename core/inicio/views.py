from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class InicioView(LoginRequiredMixin, TemplateView):
    template_name = 'inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        return context