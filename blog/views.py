from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Post

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.db.models import Q

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

# BUSCAR POST
def buscar_post(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        post = Post.objects.filter(
            Q(title__contains=busqueda) | Q(text__contains=busqueda)
        )
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