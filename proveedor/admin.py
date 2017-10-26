from django.contrib import admin
from .models import Proveedor

class AdminProveedor(admin.ModelAdmin):
	list_display = ['cedula','telefono','direccion','nombre_empresa','direccion_empresa','telefono_empresa']
	search_fields=['cedula']
	class Meta:
	 	model= Proveedor
admin.site.register(Proveedor,AdminProveedor)  