from django.urls import path
from .views import (
    buscar_post, about,
    PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView
)

urlpatterns = [
    path("buscar-post/", buscar_post, name="buscar_post"),
    path("about/", about, name="about"),
    path("posts/", PostListView.as_view(),name="posts"),
    path("ver-post/<int:pk>/", PostDetailView.as_view(), name="ver_post"),
    path("subir-posts/", PostCreateView.as_view(), name="subir_post"),
    path("eliminar-post/<int:pk>/", PostDeleteView.as_view(), name="eliminar_post"),
    path("editar-post/<int:pk>/", PostUpdateView.as_view(), name="editar_post"),
]