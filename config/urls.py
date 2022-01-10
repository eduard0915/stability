"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings as setting, settings
from core.home.views import HomeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name='home'),
    path('user/', include('core.user.urls')),
    path('inicio/', include('core.inicio.urls')),
    path('login/', include('core.login.urls')),
    path('company/', include('core.company.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if setting.DEBUG:
    urlpatterns += static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)
