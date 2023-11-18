from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from .models import Usuario, Post
from .forms import UserForm

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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

# BUSCAR POST
def buscar_post(request):
    if request.method == "POST":
        data = request.POST
        post = Post.objects.filter(name__contains=data["search"].title())

        return render(
            request=request,
            template_name="blog/posts.html",
            context={"post":post}
        )

# VER POSTS
class PostListView(ListView):
    model = Post
    template_name = "blog/posts.html"

# VER DETALLES
class PostDetailView(DetailView):
    model = Post
    success_url = reverse_lazy("posts")

# SUBIR POSTS
class PostCreateView(CreateView):
    model = Post
    fields = ['title','author','text','post']
    template_name = "blog/subir.html"
    success_url = reverse_lazy("posts")

# ELIMINAR POSTS
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("posts")
    
# EDITAR
class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/editar_post.html"
    fields = ['title','author','text','post']
    success_url = reverse_lazy("posts")