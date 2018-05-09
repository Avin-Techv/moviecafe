from django.shortcuts import render
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import FormView,TemplateView
from accounts.forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth import *
from django.contrib.auth import get_user_model

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

class RegisterUserView(FormView):

        template_name = "accounts/register.html"
        form_class = RegisterUserForm
        success_url = 'accounts/home/'

        def form_valid(self, form):
            get_user_model().objects.create_user(form.cleaned_data.get('email'),
                                                 form.cleaned_data.get('password'),
                                                 form.cleaned_data.get('mobile_no'),
                                                 form.cleaned_data.get('name')
                                                 )
            return render(self.request,"accounts/home.html")

class LoginUserView(FormView):

        template_name = "accounts/login.html"
        form_class = LoginUserForm

        def post(self, request, *args, **kwargs):
                email = request.POST['email']
                password = request.POST['password']
                # try:
                print(email, password, "")
                user = authenticate(request, email=email, password=password)
                print("auth", str(authenticate(email=email, password=password)))


                if user is not None:
                        login(request, user)
                        return render(request, 'accounts/home.html')

                else:
                        return HttpResponse("invalid")

class View(FormView):
        # pass
        template_name = "accounts/addmovie.html"
        form_class = MovieAddForm
        success_url = '/thanks/'

        def form_valid(self, form):

                form.save()
                return render(self.request, "accounts/home.html")

class HomeUserView(FormView):
        template_name = "accounts/home.html"
        form_class = MovieAddForm
        success_url = 'accounts/home/'

        def form_valid(self, form):
                return render(self.request, 'accounts/home.html')

class MovieAddForm(FormView):
    pass