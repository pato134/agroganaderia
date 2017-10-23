from django.shortcuts import render
from cart.cart import Cart

def factura_nuevo(request):
	if  request.method == 'POST':
		cart= Cart(request)
		print(cart.summary())
	context={
		"cart":cart,
	}
	return render(request,'productos/cart.html',context) 
