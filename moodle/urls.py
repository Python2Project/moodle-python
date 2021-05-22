from django.urls import path, re_path
from .views import LoginAPIView, RegistrationAPIView, StudentProfileView

urlpatterns = [
    path('teacher/add/', RegistrationAPIView.as_view(), name='teacher_registration'),
    path('student/add/', RegistrationAPIView.as_view(), name='student_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    re_path(r'^profile', StudentProfileView.as_view()),
]
