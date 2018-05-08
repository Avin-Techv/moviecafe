from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email']

    # validate password

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError('Password dont match !!!')

        return cd['password2']


class LoginUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())

    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ['username','password']

class MovieAddForm(forms.ModelForm):
    movie_title = forms.CharField(widget=forms.CharField)