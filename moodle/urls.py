from django.urls import path, re_path
from . import views
from .views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]