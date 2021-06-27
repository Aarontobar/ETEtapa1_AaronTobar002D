from django.urls import path, include
from .views import inicio, proveedo, eliminar, quitar, formproveedor

urlpatterns= [
    path('inicio/', inicio, name="inicio"),
    path('proveedor/', proveedo, name="proveedor"),
    path('eliminar/', eliminar, name="eliminar"),
    path('quitar/', quitar, name="quitar"),
    path('formproveedor/', formproveedor, name="formproveedor")
]