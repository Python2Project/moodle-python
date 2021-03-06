from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from .models import User, Student, Teacher, Course, GroupToCourse, TeacherToCourse, Task, StudentToTask, Groups
from rest_framework_jwt.settings import api_settings

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'is_student', 'is_teacher']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if user.is_teacher:
            user.is_student = False
            Teacher.objects.create_user(user)
        if user.is_student:
            user.is_teacher = False
            Student.objects.create_user(user)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return {
            'email': user.email,
            'token': jwt_token
        }


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class GroupToCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupToCourse
        fields = '__all__'


class TeacherToCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherToCourse
        fields = '__all__'


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    task_name = serializers.CharField()
    deadline = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    created_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task_name = validated_data.get('task_name', instance.task_name)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.save()
        return instance


class StudentToTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentToTask
        fields = '__all__'