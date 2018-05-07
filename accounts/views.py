from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from accounts.forms import RegisterUserForm
from django.contrib.auth.models import User
from django.db import models

# Create your views here.

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return render(self.request,'userhome.html')
        #return HttpResponse('User Registered')