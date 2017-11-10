from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Producto
from .forms import ProductoForm
from cart.cart import Cart


def producto_nuevo(request):
	if  request.method == 'POST':
		producto_form = ProductoForm(request.POST, request.FILES)
		if producto_form.is_valid():
			producto=producto_form.save()
			producto.save()
			return redirect('productos:listar_productos')
	else:
		producto_form=ProductoForm()


	return render(request, 'productos/producto_form.html',{'form':producto_form})

def gestionar_proformas(request):
	productos=Producto.objects.all()
	context={
			'productos':productos,
	}

	return render(request,'productos.html',context)

def gestionar_factura(request):
	productos=Producto.objects.all()
	context={
			'productos':productos,
	}

	return render(request,'productos.html',context)

@login_required()
def listar_productos(request):
	productos=Producto.objects.all()
	context={
			'productos':productos,
	}

	return render(request,'productos/producto_list.html',context)

def productoa_nuevo(request):
	return render(request, 'productos_agricolas.html',{}) 
@login_required()
def listar_agricolas(request):
	productos=Producto.objects.filter(tipo_producto__nombre="agricola")
	context={
			'productos':productos,
	}

	return render(request,'productos/producto_list.html',context)

def accesorios_nuevo(request):
	return render(request, 'accesorios.html',{}) 

@login_required()
def listar_accesorios(request):
	productos=Producto.objects.filter(tipo_producto__nombre="accesorios")
	context={
			'productos':productos,
	}

	return render(request,'productos/producto_list.html',context)

@login_required()
def add_to_cart(request, id_producto, quantity):
	producto = Producto.objects.get(id=id_producto)
	cart = Cart(request)
	# Controlamos que haya stock dismponible
	if producto.stock <= 0:
		messages.error(request, 'Ya no nos quedan productos '+producto.nombre)
	else:
		cart.add(producto, producto.valor_producto, quantity)
	response= HttpResponseRedirect(request.GET.get('next'))
	return response
@login_required()
def remove_from_cart(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    cart = Cart(request)
    cart.remove(producto)
    response= HttpResponseRedirect(request.GET.get('next'))
    return response

@login_required()
def get_cart(request):
	cart= Cart(request)
	context={
				"cart":cart,
	}
	return render(request,'productos/cart.html',context)
	
