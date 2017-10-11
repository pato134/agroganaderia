from django.shortcuts import render
from django.shortcuts import redirect

#def base(request):
#	return render(request, "base.html", {})

def mostrar_inicio(request):
	return render(request, 'index.html',{})

def mostrar_galeria(request):
	return render(request, 'galeria.html',{})

def mostrar_quienessomos(request):
	return render(request, 'quienessomos.html',{})

def mostrar_Productos(request):
	return render(request, 'productos.html',{})

def mostrar_proveedores(request):
	return render(request, 'proveedores.html',{})

def mostrar_facturacion(request):
	return render(request, 'facturacion.html',{})

def mostrar_proformas(request):
	return render(request, 'proformas.html',{})

def mostrar_contactos(request):
	return render(request, 'contactos.html',{})

def mostrar_elements(request):
	return render(request, 'elements.html',{})

def mostrar_indexvideo(request):
	return render(request, 'index-video.html',{})

def mostrar_servicessingle(request):
	return render(request, 'services-single.html',{})

def mostrar_clientes(request):
	return render(request, 'clientes.html',{})

def mostrar_team(request):
	return render(request, 'team.html',{})

def mostrar_testimonials(request):
	return render(request, 'testimonials.html',{})

def login(request):
	return render(request, 'login.html',{})

