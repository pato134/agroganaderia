from django.shortcuts import render
from cart.cart import Cart
from .models import Factura,Detalle
from datetime import date
from django.db import transaction
from decimal import *

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
			print cantidad
			producto.stock -= int(cantidad)
			producto.save()
			detalle= Detalle(
				factura=factura,
				producto=item.get_product(),
				cantidad=cantidad,
				precio=item.total_price
				)
			detalle.save()
			print(detalle)

		print(cart.summary())
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

	