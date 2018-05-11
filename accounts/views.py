from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import *
from django.contrib.auth import get_user_model, logout
from django.views.generic.list import ListView
from django.utils import timezone
from .forms import *
from .models import *


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
            return render(self.request, "accounts/home.html")


class LoginUserView(FormView):

        template_name = "accounts/login.html"
        form_class = LoginUserForm

        def post(self, request, *args, **kwargs):
                print("Hai")
                email = request.POST.get('email')
                password = request.POST.get('password')
                # try:
                user = authenticate(email=email, password=password)
                print("auth", str(authenticate(email=email, password=password)))
                if user is not None:
                        login(request, user)
                        return render(request, 'accounts/home.html')
                else:
                        return HttpResponse("invalid")


class ViewMovie(FormView):
        # pass
        template_name = "accounts/addmovie.html"
        form_class = MovieAddForm
        success_url = '/thanks/'

        def form_valid(self, form):
                moviename = form.cleaned_data['moviename']
                hours = form.cleaned_data['hours']
                category = form.cleaned_data['category']
                poster = form.cleaned_data['poster']
                print(poster)

                Item.objects.create(moviename=moviename, hours=hours, category=category, poster=poster)
                return render(self.request, "accounts/home.html")


class HomeUserView(ListView):
        template_name = "accounts/home.html"
        form_class = MovieAddForm
        success_url = 'accounts/home/'

        model = Item

        def form_valid(self):
                return render(self.request, 'accounts/home.html')

# class DetailsView(ListView):
#         template_name = "accounts/seemovie.html"
#         model = Item
#         success_url = 'accounts/seemovie.html'x


class IndexView(ListView):
        template_name = 'accounts/seemovie.html'
        model = Item
        pagenate_by = 10


# class DetailUserView(generic.DetailView):
#     model = Item
#     template_name = 'accounts/seemovie.html'
#     context_object_name = 'context_movie'

# class LogoutView(ListView):
#     template_name = 'accounts/logged_out.html'
#     model = Item
#
#     def logout_view(self, request):
#         logout(request)
#         return render(self.request, "accounts/home.html")

class LogoutView(FormView):
    def get(self, request, *args, **kwargs):
        # print (self.request.user.username)
        logout(request)
        return HttpResponseRedirect('/')


class ArticleListView(ListView):

    model = Item
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

