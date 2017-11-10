# Create your views here.
from datetime import date
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from cart.cart import Cart
#from django.urls import reverse_lazy
from .models import Proforma,DetalleProforma
from .forms import ProformaForm


from django.core.urlresolvers import reverse_lazy


class ProformaCreate(CreateView):
    model = Proforma
    form_class = ProformaForm
    success_url = reverse_lazy('proforma:list')

    #fields = ['s_individuales']

class ProformaUpdate(UpdateView):
    model = Proforma

class ProformaDetail(DetailView):
    model = Proforma

class AuthorDelete(DeleteView):
    model = Proforma
    success_url = reverse_lazy('proforma-list')

class ProformaList(ListView):
	model = Proforma	


def proforma_nuevo(request):
	cart= Cart(request)
	ultima_proforma=Proforma.objects.all().last()
	if not ultima_proforma:
		numero=1  
	else:
		numero=ultima_proforma.numero+1

	#instancia factura
	iva=request.POST.get("iva_hidden")
	total=request.POST.get("total_hidden")

	proforma= Proforma(
		numero=numero,
		cliente=request.user,
		fecha=date.today(),
		iva=iva,
		total=total,
		)
	proforma.save()
	#instancia de detalle
	for item in cart.cart.item_set.all():
		detalle= DetalleProforma(
			proforma=proforma,
			producto=item.get_product(),
			cantidad=item.quantity,
			precio=item.total_price
			)
		detalle.save()

	print(cart.summary())
	context={
		"cart":cart,
		"user":request.user,
		"proforma":proforma,	
	}
	return render(request,'proformas/proforma.html',context) 

def proforma_list(request):
	proforma= Proforma.objects.filter(cliente=request.user)
	context={
		"proformas":proforma,
	}
	return render(request,'proformas/proforma_list.html',context)

def ver_proforma(request,id_proforma):
	proforma=Proforma.objects.get(id=id_proforma)	
	context={
		"proforma":proforma,
		"user":proforma.cliente,
	}
	return render(request,'proformas/proforma.html',context) 

