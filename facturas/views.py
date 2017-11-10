from django.shortcuts import render, redirect
from cart.cart import Cart
from datetime import date
from django.core.mail import send_mail

from django.contrib import messages
from django.db import transaction
from decimal import *
from .models import Factura,Detalle

@transaction.atomic
def factura_nuevo(request):
	cart= Cart(request)
	if  request.method == 'POST':
		ultima_factura=Factura.objects.all().last()
		if not ultima_factura:
			numero=1 
		else:
			numero=ultima_factura.numero+1

		#instancia factura
		iva=request.POST.get("iva_hidden")
		total=request.POST.get("total_hidden")
		print("iva")
		print(iva)
		print(total)

		factura= Factura(
			numero=numero,
			cliente=request.user,
			fecha=date.today(),
			iva=iva,
			total=total,
 
			)
		factura.save()

		#instancia de detalle
		for item in cart.cart.item_set.all():
			producto = item.get_product()
			quantity_id = 'quantity'+ str(producto.pk)
			cantidad=request.POST.get(quantity_id)
			producto.stock -= int(cantidad)
			if producto.stock < 0:
				print('No quedan productos')
				factura.delete()
				messages.error(request, 'Lo sentimos, no nos quedan productos para '+producto.nombre)
				return redirect('productos:get_cart')
			producto.save()
			detalle= Detalle(
				factura=factura,
				producto=item.get_product(),
				cantidad=cantidad,
				precio=item.total_price
				)
			detalle.save()
		email_factura(factura)
	context={
		"cart":cart,
		"user":request.user,
		"factura":factura,

		
	}
	return render(request,'factura/factura.html',context) 


def factura_list(request):
	factura= Factura.objects.filter(cliente=request.user)
	context={
		"facturas":factura,
	}
	return render(request,'factura/ver_mis_facturas.html',context)

def ver_factura(request,id_factura):
	factura=Factura.objects.get(id=id_factura)	
	context={
		"factura":factura,
		"user":factura.cliente,
	}
	return render(request,'factura/factura.html',context) 

	
# Envio de mail
def email_factura(factura):
	print('ENVIO DE EMAIL')
	print(factura.cliente.email)
	subject = 'Notificacion Factura'
	message = 'SU FACTURA SE HA REALIZADO CON EXITO\n'
	message = '\nFactura Nro.: '+str(factura.numero)+'\n'
	for detalle in factura.detalle_set.all():
		producto = detalle.producto
		message += '\n'+producto.nombre
		message += '\t'+str(detalle.cantidad)
		message += '\t'+str(detalle.precio)
	message += '\nIva: '+str(factura.iva)
	message += '\nTotal: '+str(factura.total)
	

	send_mail(
	    subject,
	    message,
	    'espinosap430@gmail.com',
	    ['espinosap430@gmail.com', factura.cliente.email],
	    fail_silently=False,
	)