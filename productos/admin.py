from django.contrib import admin
from .models import Producto,TipoProducto
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class AdminProducto(ImportExportModelAdmin,admin.ModelAdmin):
	list_display=['id','image','nombre', 'tipo_producto','valor_producto','fecha_vencimiento','stock']
	search_fields=['nombre']
	class Meta:
		model=Producto

admin.site.register(Producto,AdminProducto)

class AdminTipoProducto(ImportExportModelAdmin,admin.ModelAdmin):
	list_display=['nombre']
	search_fields=['nombre']
	class Meta:
		model= TipoProducto 

admin.site.register(TipoProducto,AdminTipoProducto)


