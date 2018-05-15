from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('', views.HomeUserView.as_view(), name="home"),
    path('register', views.RegisterUserView.as_view(), name="reg"),
    path('login', views.LoginUserView.as_view(), name="login"),
    path('viewmovie', views.ViewMovie.as_view(), name="viewmovie"),
    path('see-movie', views.IndexView.as_view(), name="seemovie"),
    # path('logged_out', views.LogoutView.as_view(), name="logged_out"),
    path('logout/', auth_views.logout, {'next_page': 'accounts:home'}, name='logout'),

    path('signup', views.signup, name='signup'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    path('activate/<slug:uidb64>/<slug:token>)/', views.activate, name='activate'),
]
