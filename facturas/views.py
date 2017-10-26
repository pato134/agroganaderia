from django.shortcuts import render
from cart.cart import Cart
from .models import Factura,Detalle
from datetime import date
from django.db import transaction

@transaction.atomic
def factura_nuevo(request):
	if  request.method == 'POST':
		cart= Cart(request)
		ultima_factura=Factura.objects.all().last()
		numero=ultima_factura.numero+1

		#instancia factura
		factura= Factura(
			numero=numero,
			cliente=request.user,
			fecha=date.today()
			)
		factura.save()
		#instancia de detalle
		for item in cart.cart.item_set.all():
			detalle= Detalle(
				factura=factura,
				producto=item.get_product(),
				cantidad=item.quantity,
				precio=item.total_price
				)
			detalle.save()
			print detalle

		print(cart.summary())
	context={
		"cart":cart,
		"user":request.user,
		"factura":factura,
		
	}
	return render(request,'factura/factura.html',context) 
