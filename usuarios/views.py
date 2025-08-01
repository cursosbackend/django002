from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .form import FormularioRegistroUsuario

# Create your views here.

class RegistroUsuario(SuccessMessageMixin, CreateView):
    form_class =  FormularioRegistroUsuario
    template_name = "usuarios/registro.html"
    success_url = reverse_lazy('login')
    success_message = 'usuario registrado correctamente'


class LoginUsuario(LoginView):
    template_name = 'usuarios/login.html'



class LogoutUsuario(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('home')
    http_method_names = ['get','post']







