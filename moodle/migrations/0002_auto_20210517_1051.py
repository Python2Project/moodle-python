# Generated by Django 3.0 on 2021-05-17 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]