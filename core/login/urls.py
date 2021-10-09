from django.contrib.auth.views import LogoutView
from django.urls import path

from core.login.forms import EmailValidationForgotPassword
from core.login.views import *



urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("reset/password_reset/", FormResetPasswordView.as_view(form_class=EmailValidationForgotPassword), name='password_reset'),
    path("reset/(<uidb64>[0-9A-Za-z_])/(<token>.)/", ResetConfirmPasswordView.as_view(), name='password_reset_confirm'),
    path("reset/done/", ResetCompletePasswordView.as_view(), name='password_reset_complete'),
]
