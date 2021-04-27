from django.shortcuts import render,redirect
from .models import Item,Category
from django.http import HttpResponse
from django.template import loader
from .forms import Taskform,UserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import authenticate_user

# Create your views here.


@login_required(login_url="login")
def display(request):
    task_list = Item.objects.filter(user = request.user)

    Count = task_list.filter(complete=False).count()
    
    
    get_input = request.GET.get("search-area")

    if get_input != ' ' and get_input is not None:
        task_list = task_list.filter(title__startswith = get_input)
    else:
        get_input = "Search"

        
    return render(request,'todoapp/display.html',{'task_list':task_list,'Count':Count,'get_input':get_input})

@login_required(login_url="login")
def task_create(request):

    context ={}

    form = Taskform(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('display')

    context['form'] = form
    return render(request,'todoapp/task_create.html',context)

@login_required(login_url="login")
def task_view(request,pk):

    item = Item.objects.get(pk=pk)
    context = {
        'item':item,
    }

    return render(request,'todoapp/task_view.html',context)

@login_required(login_url="login")
def task_update(request,id):

    details = Item.objects.get(id=id)

    form = Taskform(request.POST or None, instance=details)

    if form.is_valid():
        form.save()

        return redirect('display')

    context = {
        'form':form
    }

    return render(request,'todoapp/task_update.html',context)

@login_required(login_url="login")
def task_delete(request,id):

    item_delete = Item.objects.get(id=id)

    if request.method == 'POST':
        item_delete.delete()
        return redirect('display')

    context={
        'item_delete':item_delete
    }

    return render(request,'todoapp/task_delete.html',context)

@authenticate_user
def register(request):

    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get("username")
            messages.success(request,f'Welcome {user_name} your account is created.')
            return redirect('login')            
    context={
        'form':form
    }
    return render(request,'todoapp/register.html',context)


    
@authenticate_user
def loginpage(request):

    if request.method == "POST":

            username = request.POST.get('uname')
            password = request.POST.get('psw')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('display')

            else:
                messages.info(request,'Username or Password is incorrect')

        
    context={}
    return render(request,'todoapp/login.html',context)

    

def logoutuser(request):
    logout(request)
    return redirect('login')

    








    




