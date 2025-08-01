from django.urls import path
from .views import registro
from django.contrib.auth import views as v


urlpatterns = [
    path("registro/",  registro, name="registro"),
    path("login/", v.LoginView.as_view(template_name='usuarios/login.html'), name="login"),
    path("logout/", v.LogoutView.as_view(), name="logout"),
    
]
