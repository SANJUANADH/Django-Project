from email import message
from inspect import Parameter
from typing import Any
from django.shortcuts import render, redirect
from django.urls import is_valid_path
from .forms import MyRegisterForm
from django.contrib import messages
from .models import RegisterForm
# Create your views here.
def home(request):
    data=RegisterForm.objects.all()
    if(data!=''):
        return render(request,"home.html", {'data': data})
    else:
        return render(request,"home.html")

def insert (request):
    if request.method=='POST':
       form = MyRegisterForm(request.POST)
       if form.is_valid():
            try:
               form.save()
               messages.success(request, "Registration Successfully Completed")
               return redirect("Home")

            except:
                 pass

         
          
    else:
        form=MyRegisterForm()
    return render(request, "register.html", {'form' : form})


    def update(request):
        return render(request, "update.html")

