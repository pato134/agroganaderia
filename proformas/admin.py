from django.contrib import admin
from .models import Proforma,DetalleProforma

class AdminProforma(admin.ModelAdmin):
	list_display = ['id','numero','cliente','fecha','iva','total']
	search_fields=['numero']
	class Meta:
	 	model= Proforma
admin.site.register(Proforma,AdminProforma)

class AdminDetalleProforma(admin.ModelAdmin):
	list_display = ['id','proforma','producto','cantidad','precio']
	search_fields=['proforma']
	class Meta:
	 	model= DetalleProforma
admin.site.register(DetalleProforma,AdminDetalleProforma)# Register your models here.
