from django.urls import path, include
from .views import inicio, proveedo

urlpatterns= [
    path('inicio/', inicio, name="inicio"),
    path('proveedor/', proveedo, name="proveedor")
]