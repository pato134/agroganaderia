from django.contrib import admin
from .models import Producto,TipoProducto


# Register your models here.
class AdminProducto(admin.ModelAdmin):
	list_display=['id','image','nombre', 'tipo_producto','valor_producto','fecha_vencimiento']
	search_fields=['nombre']
	class Meta:
		model=Producto

admin.site.register(Producto,AdminProducto)

class AdminTipoProducto(admin.ModelAdmin):
	list_display=['nombre']
	search_fields=['nombre']
	class Meta:
		model= TipoProducto 

admin.site.register(TipoProducto,AdminTipoProducto)
