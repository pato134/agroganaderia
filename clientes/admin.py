from django.contrib import admin

# Register your models here.


from .models import Cliente

class AdminCliente(admin.ModelAdmin):
	list_display = ['user', 'cedula','direccion','telefono','genero','edad','lugar']
	search_fields=['cedula']
	class Meta:
	 	model= Cliente
admin.site.register(Cliente,AdminCliente)