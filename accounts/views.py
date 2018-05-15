from .forms import *
from .models import *
from django.utils import timezone
from django.views.generic import FormView
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

""" import for email verification """

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import RegisterUserForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


class RegisterUserView(FormView):

        template_name = "accounts/register.html"
        form_class = RegisterUserForm
        success_url = 'accounts/register_success.html'

        def form_valid(self, form):
            get_user_model().objects.create_user(form.cleaned_data.get('email'),
                                                 form.cleaned_data.get('password'),
                                                 form.cleaned_data.get('mobile_no'),
                                                 form.cleaned_data.get('name')
                                                 )
            return render(self.request, "accounts/register.html")


class LoginUserView(FormView):

        template_name = "accounts/login.html"
        form_class = LoginUserForm

        def post(self, request, *args, **kwargs):
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


class ArticleListView(ListView):

    model = Item
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


""" social login  """


@login_required
def home(request):
    return render(request, 'accounts/login.html')


def home(request):
    return render(request, 'accounts/home.html')


""" function to implement email verification """


def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your movie rating account.'
            # message = render_to_string('accounts/acc_active_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })

            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegisterUserForm()
    return render(request, 'accounts/signup.html', {'form': form})


""" activate user account through activation link """


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserProfile.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
