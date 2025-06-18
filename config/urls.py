from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings as setting, settings
from core.home.views import HomeView
from core.homepage.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name='home'),
    path('user/', include('core.user.urls')),
    path('start/', include('core.start.urls')),
    path('login/', include('core.login.urls')),
    path('company/', include('core.company.urls')),
    path('condition/', include('core.condition.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if setting.DEBUG:
    urlpatterns += static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)
