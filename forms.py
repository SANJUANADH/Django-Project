from django import forms
#from django.db import ModelForm
#from django.forms import Form
from .models import RegisterForm

class MyRegisterForm(forms.ModelForm):
    class Meta:
        model= RegisterForm
        fields= ["name", "age", "address", "contact", "email"]


