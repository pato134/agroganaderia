from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Cliente
# Register your models here.
class AdminCliente(admin.ModelAdmin):
	list_display=['direccion','telefono','genero','edad']
	#search_fields=['id_cliente']
	class Meta:
		model=Cliente 

admin.site.register(Cliente,AdminCliente)