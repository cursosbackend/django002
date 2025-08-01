from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request, "app/home.html", {"productos": productos})


@login_required
def about(request):
    return render(request, "app/about.html", {})