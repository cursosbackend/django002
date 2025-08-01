

from django.urls import path
from .views import home, about, ProductoDetalle

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("producto/<int:pk>/",ProductoDetalle.as_view(), name="detalle"),
]
