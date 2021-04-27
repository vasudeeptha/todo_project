from django import forms
from .models import Item,Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Taskform(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["user","title","description","complete","created","due_date","category"]
        exclude = ["user"]

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
