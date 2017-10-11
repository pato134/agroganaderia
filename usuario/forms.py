from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'is_staff',
			'is_active',
			'date_joined',
			'is_superuser',
		]
		labels = {
			'username': 'Nombre de usuario',
			'first_name': 'Nombres',
			'last_name': 'Apellidos',
			'email': 'Correo',
			'is_staff':'Acceder',
			'is_active':'Activo',
			'date_joined':'Fecha de Registro',
			'is_superuser': 'Es administrador',

		}