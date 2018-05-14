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
    path('seemovie', views.IndexView.as_view(), name="seemovie"),
    path('logged_out', views.LogoutView.as_view(), name="logged_out"),

    url(r'^signup/$', views.signup, name='signup'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    path('activate/<slug:uidb64>/<slug:token>)/', views.activate, name='activate'),
]
