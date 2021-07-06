from django.urls import path, include
from .views import inicio, proveedo, eliminar, quitar, formproveedor, modproveedor, llamar, modificar, contrasenna

urlpatterns= [
    path('inicio/', inicio, name="inicio"),
    path('proveedor/', proveedo, name="proveedor"),
    path('eliminar/', eliminar, name="eliminar"),
    path('quitar/', quitar, name="quitar"),
    path('formproveedor/', formproveedor, name="formproveedor"),
    path('modproveedor/', modproveedor, name="modproveedor"),
    path('llamar/', llamar, name="llamar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('contrasenna/', contrasenna, name="contrasenna")
]