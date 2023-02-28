from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Tasks,Users

class Taskcreate(forms.ModelForm):
    class Meta:
        model=Tasks
        fields= '__all__'

class usercreate(forms.ModelForm):
    class Meta:
        model=Users
        fields= ('username','phone','password','full_name','email','employer'  )


