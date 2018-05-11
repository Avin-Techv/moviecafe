from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile, Item
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    name=forms.CharField(max_length=10)
    email=forms.EmailField(max_length=50)
    mobile_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
            model = UserProfile
            fields = ['name', 'email', 'mobile_no', 'password']

    # validate password

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError('Password dont match !!!')

        return cd['password2']


class LoginUserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ['email', 'password']


class MovieAddForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['moviename', 'hours', 'category', 'poster']


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')


class Meta:
    model = User
    fields = ('username', 'email', 'password')

