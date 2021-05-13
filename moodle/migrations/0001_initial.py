# Generated by Django 3.2 on 2021-04-29 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255)),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(help_text='Enter an email, please!', max_length=255, unique=True)),
                ('firstname', models.CharField(help_text='Enter your First Name, please!', max_length=255)),
                ('lastname', models.CharField(help_text='Enter your Last Name, please!', max_length=255)),
                ('groupname', models.CharField(help_text='Enter your email, please!', max_length=255)),
                ('user_picture', models.FileField(upload_to='images/student/')),
                ('password', models.CharField(help_text='Enter your password!', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=255)),
                ('deadline', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(help_text='Enter an email, please!', max_length=255, unique=True)),
                ('firstname', models.CharField(help_text='Enter your First Name, please!', max_length=255)),
                ('lastname', models.CharField(help_text='Enter your Last Name, please!', max_length=255)),
                ('user_picture', models.FileField(upload_to='images/teacher/')),
                ('password', models.CharField(help_text='Enter your password!', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherToCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentToTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('submission_document', models.FileField(upload_to='files/tasks/')),
                ('grade', models.IntegerField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.task')),
            ],
        ),
        migrations.CreateModel(
            name='StudentToCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grade', models.IntegerField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.student')),
            ],
        ),
    ]