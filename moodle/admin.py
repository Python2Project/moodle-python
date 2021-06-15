from django.contrib import admin
from .models import Student, StudentToTask, GroupToCourse, Task, Teacher, TeacherToCourse, Course, User

admin.site.register(User)
admin.site.register(Student)
admin.site.register(StudentToTask)
admin.site.register(GroupToCourse)
admin.site.register(Task)
admin.site.register(Teacher)
admin.site.register(TeacherToCourse)
admin.site.register(Course)


