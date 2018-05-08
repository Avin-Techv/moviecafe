from  django import forms
from django.contrib.auth.models import User
from .models import *


class RegisterUserForm(forms.ModelForm):
    name=forms.CharField(max_length=10)
    email=forms.EmailField(max_length=50)
    mobile_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
            model = UserProfile
            fields =['name', 'email', 'mobile_no','password']


class LoginUserForm(forms.Form):
        email = forms.EmailField(max_length=50)
        password = forms.CharField(widget=forms.PasswordInput)