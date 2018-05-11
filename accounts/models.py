from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, mobile_no=None, name=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mobile_no=mobile_no,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name, mobile_no):
        user = self.create_user(email, password=password, name=name, mobile_no=mobile_no)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Invalid Mobile Number !!!")
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    mobile_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    is_staff = models.BooleanField(('staff status'), default=False)
    is_superuser = models.BooleanField(('staff status'), default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile_no']


class Item(models.Model):

    moviename = models.CharField(max_length=50)
    hours = models.CharField(max_length=90)
    category = models.CharField(max_length=10)
    poster = models.ImageField(upload_to='accounts/images', default="accounts/images/default_poster.jpg")
    # def __str__(self):
    #     return self.name + ": " + str(self.movie_images)
    
    def __str__(self):
        return self.moviename