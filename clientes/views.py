from django.shortcuts import render
from django.shortcuts import redirect
from .models import Cliente
from .forms import UsuarioCreationForm, CLienteForm

def mostrar_clientes(request):
	return render(request, 'clientes.html',{})

def registrarse(request):
	if request.method == 'POST':
		#form_user= UsuarioCreationForm(request.POST)
		form_cliente= CLienteForm(request.POST)
		if  form_cliente.is_valid():
			#form_user.save()
			form_cliente.save()
	else:
		#form_user=UsuarioCreationForm()
		form_cliente=CLienteForm()
	context={
			#'form_user': form_user,
			'form_cliente': form_cliente,
			}
	return render(request, 'clientes/registro.html',context)

	
