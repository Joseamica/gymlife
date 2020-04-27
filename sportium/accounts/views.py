from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST.get('last_name', False)
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST.get('password1', False)
        password2 = request.POST.get('password2', False)

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(
                    request, "Ya existe un nombre de usuario {}".format(username))
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("Email Taken")
                messages.info(
                    request, "Ya existe un correo electronico con la direccion de {}".format(email))
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User Created')
                return redirect('login')
        else:
            messages.info(request, "Las contraseñas no coinciden")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'registration/register.html')


def login(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password', False)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Usuario y contraseña incorrecto')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')
