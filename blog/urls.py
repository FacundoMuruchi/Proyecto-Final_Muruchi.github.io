from django.urls import path
from .views import (
    crear_cuenta, exito, buscar_post, usuarios,
    PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView
)

urlpatterns = [
    path("cuenta/", crear_cuenta,name="cuenta"),
    path("posts/", PostListView.as_view(),name="posts"),
    path("subir-posts/", PostCreateView.as_view(), name="subir_post"),
    path("exito/", exito, name="exito"),
    path("buscar-post/", buscar_post, name="buscar_post"),
    path("usuarios/", usuarios, name="usuarios"),
    path("eliminar-post/<int:pk>/", PostDeleteView.as_view(), name="eliminar_post"),
    path("editar-post/<int:pk>/", PostUpdateView.as_view(), name="editar_post"),
    path("ver-post/<int:pk>/", PostDetailView.as_view(), name="ver_post")
]