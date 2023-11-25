from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Post

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

# BUSCAR POST
def buscar_post(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data.get("busqueda", "")
        post = Post.objects.filter(title__icontains=busqueda)
        
        return render(
            request=request,
            template_name="blog/posts.html",
            context={"post": post, "busqueda": busqueda}
        )

# VER POSTS
class PostListView(ListView):
    model = Post
    template_name = "blog/posts.html"

# ABOUT ME
def about(request):
    return render(request,'blog/about.html')

# VER DETALLES
class PostDetailView(DetailView):
    model = Post
    success_url = reverse_lazy("posts")

# SUBIR POSTS
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','text','post']
    template_name = "blog/subir.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.creator = self.request.user
        return super().form_valid(form)

# ELIMINAR POSTS
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("posts")
    
# EDITAR
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "blog/editar_post.html"
    fields = ['title','text','post']
    success_url = reverse_lazy("posts")