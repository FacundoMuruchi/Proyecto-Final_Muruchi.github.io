from django.urls import path
from .views import registrar, exito, login_user, CustomLogoutView, profile, AccountUpdateView


urlpatterns = [
    path("registro/", registrar,name="registro"),
    path("exito/", exito, name="exito"),
    path("login/", login_user, name="login"),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('account/', profile, name='account'),
    path('edit-account/', AccountUpdateView.as_view(), name='edit_account'),
]
