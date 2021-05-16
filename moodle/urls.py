from django.urls import path, re_path
from .views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]
