from django.http import HttpResponse
from django.shortcuts import redirect

def authenticate_user(parameter_func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('display')
        else:
            return parameter_func(request,*args,**kwargs)

    return wrapper