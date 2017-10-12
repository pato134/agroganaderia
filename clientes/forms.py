from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Cliente

class UsuarioCreationForm(UserCreationForm):
   class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        labels = {
        	'first_name': 'Nombres',
        	'last_name': 'Apellidos',

        }
        widgets = {
            'password':  forms.PasswordInput(),
        }

class CLienteForm(forms.ModelForm):

	class Meta:
		model= Cliente
		fields = ('username','password','direccion','telefono','genero','edad')