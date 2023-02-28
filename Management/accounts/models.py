from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import Group
# Create your models here.
class Users(AbstractUser):
    username = models.CharField(max_length=30,unique=False )
    phone=models.CharField(max_length=10, unique=True)
    password=models.CharField(max_length=30)
    full_name = models.CharField(max_length=100)
    user_group_id = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="user_permission_group",
                                      db_column="user_group_id", null=True)
    employer=models.CharField(max_length=30,default="None")
    email = models.EmailField(max_length=100, unique=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username',]
    objects = UserManager()


class Tasks(models.Model):
    Task_name=models.CharField(max_length=30)
    Task_Status=models.CharField(max_length=30,default="started")
    assigned_to=models.CharField(max_length=30)

    def __str__(self):
        return self.Task_name

