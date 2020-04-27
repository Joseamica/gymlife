# djangotemplates/example/urls.py

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from pages import views

urlpatterns = [
    # Notice the URL has been named
    url(r'^$', views.index, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    # url(r'^register/$', views.register, name="register"),  # <-- added
    url(r'^dashboard/$', views.dashboard, name="dashboard"),  # <-- added
    # url(r'^login/$', views.login_new, name="login_new"),  # <-- added


    # TESTING
    url(r'^testinglogin/$', views.testing_login,
        name="testinglogin"),  # <-- added
    url(r'^testing/$', views.testing_live, name="testing"),  # <-- added



]
