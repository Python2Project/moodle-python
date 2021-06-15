from django.urls import path, re_path
from .views import LoginAPIView, RegistrationAPIView, StudentProfileView, TeacherProfileView, CourseAPI, CourseDetailAPI, GroupToCourseDetailAPI, GroupToCourseAPI
from .views import TeacherToCourseAPI, TeacherToCourseDetailAPI, TaskAPI, TaskDetailAPI, StudentToTaskAPI, StudentToTaskDetailAPI, GroupsAPI, GroupDetailAPI
urlpatterns = [
    path('teacher/add/', RegistrationAPIView.as_view(), name='teacher_registration'),
    path('student/add/', RegistrationAPIView.as_view(), name='student_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    re_path(r'^student/profile', StudentProfileView.as_view()),
    re_path(r'^teacher/profile', TeacherProfileView.as_view()),
    path('course/', CourseAPI.as_view()),
    path('course/<int:pk>', CourseDetailAPI.as_view()),
    path('groupToCourse/', GroupToCourseAPI.as_view()),
    path('groupToCourse/<int:pk>', GroupToCourseDetailAPI.as_view()),
    path('teacherToCourse/', TeacherToCourseAPI.as_view()),
    path('teacherToCourse/<int:pk>', TeacherToCourseDetailAPI.as_view()),
    path('task/', TaskAPI.as_view()),
    path('task/<int:pk>', TaskDetailAPI.as_view()),
    path('studentToTask/', StudentToTaskAPI.as_view()),
    path('studentToTask/<int:pk>', StudentToTaskDetailAPI.as_view()),
    path('groups/', GroupsAPI.as_view()),
    path('groups/<int:pk>', GroupDetailAPI.as_view())
]
