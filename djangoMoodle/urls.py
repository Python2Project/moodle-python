"""djangoMoodle URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

from moodle.views import RegistrationAPIView

urlpatterns = [
    path('admin/moodle/teacher/add/', RegistrationAPIView.as_view(), name='teacher_registration'),
    path('admin/moodle/student/add/', RegistrationAPIView.as_view(), name='student_registration'),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('moodle/', include('moodle.urls')),

]

urlpatterns += [
    path('', RedirectView.as_view(url='/moodle/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
