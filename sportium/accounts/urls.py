# djangotemplates/example/urls.py

from django.conf.urls import url
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from . import views  # . means this directory

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('', TemplateView.as_view(template_name="registration/google.html")),  # <--

]
