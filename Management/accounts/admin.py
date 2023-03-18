from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Users,Tasks
class UserAdmin(UserAdmin):
    ...

admin.site.register(Users, UserAdmin)

admin.site.register(Tasks)