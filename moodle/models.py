import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.core import validators
from django.db import models
from django.urls import reverse

from moodle.manager import UserManager


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False
    )
    firstname = models.CharField(max_length=255, help_text="Enter your First Name, please!", null=False)
    lastname = models.CharField(max_length=255, help_text="Enter your Last Name, please!", null=False)
    groupname = models.CharField(max_length=255, help_text="Enter your email, please!", null=False)
    user_picture = models.FileField(upload_to='images/student/')
    password = models.CharField(max_length=255, help_text="Enter your password!", null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.firstname + self.lastname

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    credit = models.IntegerField()

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse('course', args=[str(self.id)])


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False
    )
    firstname = models.CharField(max_length=255, help_text="Enter your First Name, please!", null=False)
    lastname = models.CharField(max_length=255, help_text="Enter your Last Name, please!", null=False)
    user_picture = models.FileField(upload_to='images/teacher/')
    password = models.CharField(max_length=255, help_text="Enter your password!", null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.firstname + self.lastname

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


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
