from django.urls import path
from .views import crear_cuenta, posts, subir, subir_cuento, subir_poema, exito, buscar_post, usuarios, eliminar_poema, eliminar_cuento

urlpatterns = [
    path("cuenta/", crear_cuenta,name="cuenta"),
    path("posts/", posts,name="posts"),
    path("subir-posts/", subir, name="subir"),
    path("exito/", exito, name="exito"),
    path("subir-cuento/", subir_cuento, name="subir_cuento"),
    path("subir-poema/", subir_poema, name="subir_poema"),
    path("buscar-post/", buscar_post, name="buscar_post"),
    path("usuarios/", usuarios, name="usuarios"),
    path("eliminar-poema/<id>/", eliminar_poema, name="eliminar_poema"),
    path("eliminar-cuento/<id>/", eliminar_cuento, name="eliminar_cuento")
]