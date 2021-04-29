from django.db import models
from django.urls import reverse


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, help_text="Enter an email, please!", null=False, unique=True)
    firstname = models.CharField(max_length=255, help_text="Enter your First Name, please!", null=False)
    lastname = models.CharField(max_length=255, help_text="Enter your Last Name, please!", null=False)
    groupname = models.CharField(max_length=255, help_text="Enter your email, please!", null=False)
    user_picture = models.FileField(upload_to='images/student/')
    password = models.CharField(max_length=255, help_text="Enter your password!", null=False)

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])


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
    email = models.CharField(max_length=255, help_text="Enter an email, please!", null=False, unique=True)
    firstname = models.CharField(max_length=255, help_text="Enter your First Name, please!", null=False)
    lastname = models.CharField(max_length=255, help_text="Enter your Last Name, please!", null=False)
    user_picture = models.FileField(upload_to='images/teacher/')
    password = models.CharField(max_length=255, help_text="Enter your password!", null=False)

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('teacher', args=[str(self.id)])


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
