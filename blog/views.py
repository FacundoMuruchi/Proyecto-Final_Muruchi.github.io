from django.shortcuts import render, redirect
from .models import Usuario, Cuento, Poema
from .forms import UserForm, PoemForm, StoryForm
from django.urls import reverse

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

# CREAR CUENTA

def crear_cuenta(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user=Usuario(name=data["name"], surname=data["surname"], password=data["password"], age=data["age"], email=data["email"])
            user.save()

            url_exitosa = reverse("exito")
            return redirect(url_exitosa)
    else:
        form = UserForm()

    return render(
        request=request,
        template_name="blog/cuenta.html",
        context={"form":form}
    )
        
# CUENTA CREADA
    
def exito(request):
    return render(request, "blog/exito.html")

# VER CUENTAS

def usuarios(request):
    return render(
        request=request,
        template_name="blog/usuarios.html",
        context={"usuarios": Usuario.objects.all()}
    )

# VER POSTS

def posts(request):
    return render(request,
                  "blog/posts.html",
                  context={"cuento": Cuento.objects.all(), "poema": Poema.objects.all()})

# BUSCAR POST

def buscar_post(request):
    if request.method == "POST":
        data = request.POST
        cuento = Cuento.objects.filter(name__contains=data["search"].title())
        poema = Poema.objects.filter(name__contains=data["search"].title())

        return render(
            request=request,
            template_name="blog/posts.html",
            context={"cuento": cuento, "poema": poema}
        )

# SUBIR POSTS

def subir(request):
    return render(
        request=request,
        template_name="blog/subir.html"
    )

# CUENTO
def subir_cuento(request):
    if request.method == "POST":
        form = StoryForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            story = Cuento(name=data["name"].title(), text=data["text"], author=data["author"].title())
            story.save()

            url_exitosa = reverse("posts")
            return redirect(url_exitosa)
    else:
        form = StoryForm()

    return render(
        request=request,
        template_name="blog/subir_cuento.html",
        context={"story": form}
    )

# POEMA

def subir_poema(request):
    if request.method == "POST":
        form = PoemForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            story = Poema(name=data["name"].title(), text=data["text"], author=data["author"].title())
            story.save()

            url_exitosa = reverse("posts")
            return redirect(url_exitosa)
    else:
        form = PoemForm()

    return render(
        request=request,
        template_name="blog/subir_poema.html",
        context={"poem": form}
    )