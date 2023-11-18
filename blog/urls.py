from django.urls import path
from .views import crear_cuenta, posts, subir, exito, buscar_post, usuarios, eliminar_post

urlpatterns = [
    path("cuenta/", crear_cuenta,name="cuenta"),
    path("posts/", posts,name="posts"),
    path("subir-posts/", subir, name="subir"),
    path("exito/", exito, name="exito"),
    path("buscar-post/", buscar_post, name="buscar_post"),
    path("usuarios/", usuarios, name="usuarios"),
    path("eliminar-post/<id>/", eliminar_post, name="eliminar_post"),
]