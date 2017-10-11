from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy 
from usuario.forms import UsuarioForm
from django.shortcuts import render


class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = UsuarioForm
	success_url = reverse_lazy("productos:productos_crear")
