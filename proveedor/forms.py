from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):

	class Meta:
		model= Proveedor
		fields = ('nombres','apellidos','cedula','telefono','direccion','nombre_empresa','direccion_empresa','telefono_empresa')