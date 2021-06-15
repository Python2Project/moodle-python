from django.urls import path, re_path
from .views import LoginAPIView, RegistrationAPIView, StudentProfileView, TeacherProfileView, CourseAPI, CourseDetailAPI, StudentToCourseDetailAPI, StudentToCourseAPI
from .views import TeacherToCourseAPI, TeacherToCourseDetailAPI
urlpatterns = [
    path('teacher/add/', RegistrationAPIView.as_view(), name='teacher_registration'),
    path('student/add/', RegistrationAPIView.as_view(), name='student_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    re_path(r'^student/profile', StudentProfileView.as_view()),
    re_path(r'^teacher/profile', TeacherProfileView.as_view()),
    path('course/', CourseAPI.as_view()),
    path('course/<int:pk>', CourseDetailAPI.as_view()),
    path('studentToCourse/', StudentToCourseAPI.as_view()),
    path('studentToCourse/<int:pk>', StudentToCourseDetailAPI.as_view()),
    path('teacherToCourse/', TeacherToCourseAPI.as_view()),
    path('teacherToCourse/<int:pk>', TeacherToCourseDetailAPI.as_view())
]
