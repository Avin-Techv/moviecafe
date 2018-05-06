from django.conf.urls import url,include
from accounts.views import RegisterUserView

urlpatterns = [
    url(r'^register/$', view=RegisterUserView.as_view(),name='register'),
]

# urlpatterns = [
#     url(r'^register/', include('accounts.urls')), # add .urls after app name
# ]