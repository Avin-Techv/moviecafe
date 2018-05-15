from django.core.exceptions import ValidationError
from .models import UserProfile, Item
from django import forms


class RegisterUserForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    mobile_no = forms.IntegerField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
            model = UserProfile
            fields = ['name', 'email', 'mobile_no', 'password1', 'password2']

    # validate password

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise ValidationError('Passwords do not match !!!')

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
