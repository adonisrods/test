from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Tasks,Users
CHOICES =(
    ("Started", "Started"),
    ("Finished", "Finished"),
    ("Blocked", "Blocked"))
class Taskcreate(forms.ModelForm):
    Task_name = forms.CharField(max_length=30)
    Task_Status = forms.ChoiceField(choices=CHOICES)
    assigned_to = forms.ModelChoiceField(queryset=Users.objects.all())

    class Meta:
        model = Tasks
        fields ='__all__'

class usercreate(forms.ModelForm):
    class Meta:
        model=Users
        fields= ('username','phone','password','full_name','email','employer'  )


