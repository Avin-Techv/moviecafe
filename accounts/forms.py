from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile

class RegisterUserForm(forms.ModelForm):
    name=forms.CharField(max_length=10)
    email=forms.EmailField(max_length=50)
    mobile_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
            model = UserProfile
            fields =['name', 'email', 'mobile_no','password']

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
        model = UserProfile
        fields = ['username','password']

class MovieAddForm(forms.ModelForm):
    movie_title = forms.CharField(widget=forms.CharField)

    class Meta:
        model =UserProfile
        fields = ['movie_title']