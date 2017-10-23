from django.contrib import admin
from .models import Factura,Detalle

class AdminFacturas(admin.ModelAdmin):
	list_display = ['id','numero','cliente','fecha']
	search_fields=['numero']
	class Meta:
	 	model= Factura
admin.site.register(Factura,AdminFacturas)

class AdminDetalle(admin.ModelAdmin):
	list_display = ['id','factura','producto','cantidad','precio']
	search_fields=['factura']
	class Meta:
	 	model= Detalle
admin.site.register(Detalle,AdminDetalle)
