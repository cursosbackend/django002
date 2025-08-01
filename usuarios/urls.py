from django.urls import path
from .views import RegistroUsuario , LoginUsuario , LogoutUsuario



urlpatterns = [
    path("registro/",  RegistroUsuario.as_view() , name="registro"),
    path("login/", LoginUsuario.as_view(), name="login"),
    path("logout/", LogoutUsuario.as_view(), name="logout"),
    
]
