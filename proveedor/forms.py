from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):

	class Meta:
		model= Proveedor
		fields = ('cedula','telefono','direccion','nombre_empresa','direccion_empresa','telefono_empresa')