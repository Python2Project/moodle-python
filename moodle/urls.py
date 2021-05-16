from django.urls import path
from .views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='user_login'),
]
