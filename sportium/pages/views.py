# Create your views here.
# djangotemplates/example/views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# views.py
from django.shortcuts import redirect, render
from django.views.generic import TemplateView  # Import TemplateView

from .forms import RegisterForm
from .models import LiveVideos, NewCoach


#####TESTING#######
def testing_live(request, *args, **kwargs):

    live1 = LiveVideos()
    live1.exercise_type = 'Indoor Cycling'
    live1.coach = 'Kristel Fabre'
    live1.content_live = 'kris-fabre.png'
    live1.is_live = True
    live1.calendar_button = ''

    live2 = LiveVideos()
    live2.exercise_type = 'Yoga'
    live2.coach = 'Ari Ampudia'
    live2.content_live = 'ari-amp.png'
    live2.is_live = True
    live2.calendar_button = ''

    live3 = LiveVideos()
    live3.exercise_type = 'Funcional'
    live3.coach = 'Jose Amieva'
    live3.content_live = 'jose-amieva.png'
    live3.is_live = False
    live3.calendar_button = ''

    live4 = LiveVideos()
    live4.exercise_type = 'Funcional'
    live4.coach = 'Jose Amieva'
    live4.content_live = 'jose-amieva.png'
    live4.is_live = True
    live4.calendar_button = ''

    lives = [live1, live2, live3, live4]
    return render(request, "testing.html", {'lives': lives})


def testing_login(request, *args, **kwargs):

    return render(request, "testing_login.html")


def include_login_form(request):
    from django.contrib.auth.forms import AuthenticationForm
    form = AuthenticationForm()
    return {'login_form': form}


class HomePageView(TemplateView):
    template_name = "base.html"


# def login_view(request, *args, **kwargs):
#    return render(request, "registration/login.html")

def index(request, *args, **kwargs):

    lives = LiveVideos.objects.all()
    new_coaches = NewCoach.objects.all()

    return render(request, "base.html", {'lives': lives, 'new_coaches': new_coaches})


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")  # sting html code
    return render(request, "home.html", {})


def login_new(request, *args, **kwargs):

    # return HttpResponse("<h1>Hello World</h1>")  # sting html code
    return render(request, "registration/login_new.html", {})


def contact(request, *args, **kwargs):

    # return HttpResponse("<h1>Hello World</h1>")  # sting html code
    return render(request, "contact.html", {})


def dashboard(request, *args, **kwargs):

    # return HttpResponse("<h1>Hello World</h1>")  # sting html code
    return render(request, "dashboard.html", {})


def testing(request, *args, **kwargs):

    # return HttpResponse("<h1>Hello World</h1>")  # sting html code
    return render(request, "testing.html", {})


def blog_details_view(request, *args, **kwargs):
    return render(request, "blog-details.html")


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(response, user)
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})


@login_required(login_url='/accounts/login/')
def dashboard_view(request, *args, **kwargs):
    return render(request, "dashboard.html")
