from django.shortcuts import render
from django.shortcuts import redirect
from .models import Cliente
from .forms import UsuarioCreationForm, CLienteForm

def mostrar_clientes(request):
	return render(request, 'clientes.html',{})

def registrarse(request):
	form= CLienteForm()
	return render(request, 'clientes/registro.html',{'form':form})
	
