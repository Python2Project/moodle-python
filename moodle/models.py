from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from moodle.manager import UserManager, StudentManager, TeacherManager


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    email = models.EmailField(unique=True, null=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_student = True
    group = models.OneToOneField('Groups', on_delete=models.CASCADE, null=True)
    user_picture = models.FileField(upload_to='images/student/', null=True)

    objects = StudentManager()

    def __str__(self):
        return self.user.username

    def has_module_perms(self, app_label):
        return self.user.is_superuser

    def has_perm(self, perm, obj=None):
        return self.user.is_superuser


class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255, null=False)


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


class GroupToCourse(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey('Groups', on_delete=models.CASCADE, null=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=False)


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
    created_on = models.DateTimeField(auto_now_add=True)

