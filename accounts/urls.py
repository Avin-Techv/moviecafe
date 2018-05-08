from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'accounts'
urlpatterns = [
    path('register', views.RegisterUserView.as_view(), name="reg"),
    path('home', views.HomeUserView.as_view(), name="home"),
    path('login', views.LoginUserView.as_view(), name="login"),
    path('addmovie', views.MovieAddForm.as_view(), name="addmovie"),
]
