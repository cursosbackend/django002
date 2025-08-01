from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request, "app/home.html", {"productos": productos})


@login_required
def about(request):
    return render(request, "app/about.html", {})


class ProductoDetalle(DetailView):
    model = Producto
    template_name = 'app/detalle_producto.html'
    context_object_name = 'producto'


