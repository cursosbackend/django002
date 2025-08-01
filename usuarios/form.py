from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class FormularioRegistroUsuario(UserCreationForm):
    email = forms.EmailField(required=True)

    class meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



        



