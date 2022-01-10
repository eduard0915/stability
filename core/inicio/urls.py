from django.urls import path
from core.inicio.views import *

app_name = 'inicio'

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('inicio/notperms/', NotPermsView.as_view(), name='notperms'),
]