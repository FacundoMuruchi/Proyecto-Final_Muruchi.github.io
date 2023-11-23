from django.shortcuts import render, redirect

from .forms import UserRegisterForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

# Create your views here.

# CREAR CUENTA
def registrar(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('exito')
    else:
        form = UserRegisterForm()

    return render(
        request=request,
        template_name="profiles/registro.html",
        context={"form":form}
    )
        
# CUENTA CREADA 
def exito(request):
    return render(request, "profiles/exito.html")

# LOGIN
def login_user(request):
   next_url = request.GET.get('next')

   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')

           # COMPARA LOS DATOS DEL FORM CON LOS DE LA BD
           user = authenticate(username=usuario, password=password)

           # user puede ser un usuario o None
           if user:
               login(request=request, user=user)
               
               if next_url:
                   return redirect(next_url)
               
               return redirect('inicio')
           
   else:  # GET
       form = AuthenticationForm()

   return render(
       request=request,
       template_name='profiles/login.html',
       context={'form': form},
   )

# LOGOUT
class CustomLogoutView(LogoutView):
    template_name = 'home.html'