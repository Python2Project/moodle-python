from django.contrib.auth.base_user import BaseUserManager


class StudentManager(BaseUserManager):

    def _create_user(self, user=None):
        student = self.model(user=user)
        student.save(using=self._db)
        return student

    def create_user(self, user=None):
        return self._create_user(user)


class TeacherManager(BaseUserManager):

    def _create_user(self, user=None):
        teacher = self.model(user=user)
        teacher.save(using=self._db)
        return teacher

    def create_user(self, user=None):
        return self._create_user(user)


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The specified username must be set')

        if not email:
            raise ValueError('This email address must be set')

        if not password:
            raise ValueError('This password must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(username, email, password, **extra_fields)
