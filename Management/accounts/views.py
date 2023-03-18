from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import Taskcreate,usercreate
from.models import Tasks,Users
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
# Create your views here.


def login_user(request):
    if request.method=="POST":
        phone = request.POST.get('phone', False)
        password = request.POST.get('password', False)
        print(phone)
        print(password)
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('home')
            ...
        else:
            return redirect('login_failed')
    # Return an 'invalid login' error message.

    else:
        return render(request,'login.html', {})



def home(request):
    return render(request, 'home.html', {})


def login_failed(request):
    return render(request, 'login_failed.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')

def Create_task(request):
    context = {}
    context['form'] = Taskcreate()
    if request.method == 'POST':
        upload = Taskcreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('view_task')
        else:
            return HttpResponse("""your form data is invalid,""")

    else:
        return render(request, "create_task.html", context)

def view_all_created_task(request):
    tasks = Tasks.objects.all()
    return render(request, 'View_all_created_task.html', {'context': tasks})
def delete_task(request,id):
    obj = get_object_or_404(Tasks, id=id)
    obj.delete()
    return redirect('home')

def Update_Task(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Tasks, id=id)

    # pass the object as instance in form
    form = Taskcreate(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('home')
    # add form dictionary to context
    context["form"] = form

    return render(request, "update.html", context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Tasks, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)

#user methods

def create_users(request):
    context = {}
    context['form'] = usercreate()
    if request.method == 'POST':
        upload = usercreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('view_users')
        else:
            return HttpResponse("""your form data is invalid,""")

    else:
        return render(request, "create_user.html", context)


def View_users(request):
    users = Users.objects.all()
    return render(request, 'view_users.html', {'context': users})

def delete_user(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Users, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect('view_users')

    return render(request, "delete_view.html", context)

