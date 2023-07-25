from django.contrib.auth import views as auth_views 
# we rename the above so there is no conflict between this and the other import 

from django.urls import path 

from . import views 
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'), 
    path('signup/', views.signup, name='signup'), 
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    # .asview() is the workaround for not making view
    path('', views.logout, name='logout')
]