import re
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone, password, **extra_fields):
        user = self.model(phone=phone,password=password, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_superuser(self,phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(phone,password, **extra_fields)