from django import forms
from django.forms import ModelForm
from .models import *

class proveedorform(ModelForm):

    class Meta:
        model= proveedor
        fields= ['numero','p_nombre', 's_nombre', 'ap_paterno', 'ap_materno', 'telefono', 'direccion', 'email', 'pais', 'cantrasenna','moneda', 'imagen']
        labels= {
            'numero': 'ingrese id del proveedor',
            'p_nombre': 'nombre proveedor',
            's_nombre': 'segundo nombre',
            'ap_paterno': 'apellido paterno',
            'ap_materno': 'apellido materno',
            'telefono': 'telefono proveedor',
            'direccion': 'ingrese direccion',
            'email': 'email proveedor',
            'pais': 'seleccione pais',
            'moneda': 'seleccione moneda',
            'imagen': 'seleccione foto'
        }
        widgets={
            'numero': forms.NumberInput(
                attrs={
                    'id': 'id',
                    'name': 'id'
                }
            ),
            'p_nombre': forms.TextInput(
                attrs={
                    'id': 'nombre',
                    'name': 'nombre'
                }
            ),
            's_nombre': forms.TextInput(
                attrs={
                    'id': 's_nombre',
                    'name': 's_nombre'
                }
            ),
            'ap_paterno': forms.TextInput(
                attrs={
                    'id': 'ap_paterno',
                    'name': 'ap_paterno'
                }
            ),
            'ap_materno': forms.TextInput(
                attrs={
                    'id': 'ap_materno',
                    'name': 'ap_materno'
                }
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'id': 'telefono',
                    'name': 'telefono'
                }
            ),
            'direccion': forms.Textarea(
                attrs={
                    'id': 'direccion',
                    'name': 'direccion'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'autocomplete': 'current-password',
                    'id': 'email',
                    'name': 'email'
                }
            ),
            'pais': forms.Select(
                attrs={
                    'id': 'pais',
                    'name': 'pais'
                }
            ),
            'cantrasenna': forms.PasswordInput(
                attrs={
                    'id': 'contrasenna',
                    'name': 'contrasenna'
                }
            ),
            'moneda': forms.Select(
                attrs={
                    'id': 'moneda',
                    'name': 'moneda'
                }
            )
        }