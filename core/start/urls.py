from django.urls import path
from core.start.views import *

app_name = 'start'

urlpatterns = [
    path('', StartView.as_view(), name='start'),
    path('start/notperms/', NotPermsView.as_view(), name='not_perms'),
]
