from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile,Item

admin.site.register(UserProfile)