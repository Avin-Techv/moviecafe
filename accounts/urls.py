from django.urls import path
from . import views
from django.conf.urls import url
from .views import home

app_name = 'accounts'
urlpatterns = [
    url(r'^$', home),
    path('register', views.RegisterUserView.as_view(), name="reg"),
    path('home', views.HomeUserView.as_view(), name="home"),
    path('login', views.LoginUserView.as_view(), name="login"),
    path('viewmovie', views.ViewMovie.as_view(), name="viewmovie"),
    path('seemovie',views.IndexView.as_view(),name="seemovie"),
]
