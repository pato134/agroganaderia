from django.contrib import admin
from .models import Factura,Detalle,Pago

class AdminFacturas(admin.ModelAdmin):
	list_display = ['id','numero','cliente','fecha','iva','total']
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


class AdminPago(admin.ModelAdmin):
	list_display = ['id','factura','comprobante','sugerencia']
	search_fields=['factura']
	class Meta:
	 	model= Pago
admin.site.register(Pago,AdminPago)