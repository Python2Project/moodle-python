import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from moodle.manager import UserManager, StudentManager, TeacherManager


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = UserManager()

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_student = True
    group_name = models.CharField(max_length=255, help_text="Enter your group, please!", null=True)
    user_picture = models.FileField(upload_to='images/student/', null=True)

    objects = StudentManager()

    def __str__(self):
        return self.user.username

    def has_module_perms(self, app_label):
        return self.user.is_superuser

    def has_perm(self, perm, obj=None):
        return self.user.is_superuser


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_teacher = True
    user_picture = models.FileField(upload_to='images/teacher/', null=True)

    objects = TeacherManager()

    def __str__(self):
        return self.user.username

    def has_module_perms(self, app_label):
        return self.user.is_superuser

    def has_perm(self, perm, obj=None):
        return self.user.is_superuser


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    credit = models.IntegerField()

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse('course', args=[str(self.id)])


class TeacherToCourse(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=False)


class StudentToCourse(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, null=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=False)
    grade = models.IntegerField(null=True)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255, null=False)
    deadline = models.DateTimeField(null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('task', args=[str(self.id)])


class StudentToTask(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    submission_document = models.FileField(upload_to='files/tasks/')
    grade = models.IntegerField(null=False)
