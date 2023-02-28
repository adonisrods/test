import django
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_user, name="login" ),
    path('home/', home, name="home" ),
    path('login_failed/', login_failed, name="login_failed" ),
    path('logout/', logout_user, name="logout" ),
    path('create_task/', Create_task, name='create_task'),
    path('view_task/', View_task, name='view_task'),
    path('update_task/<int:id>', Update_Task, name='update_task'),
    path('delete/<id>', delete_view, name="delete_view" ),
    path('view_users/', View_users, name='view_users'),
    path('create_users/',create_users, name='create_users'),
    path('delete_user/<id>', delete_user, name="delete_user" ),
]


