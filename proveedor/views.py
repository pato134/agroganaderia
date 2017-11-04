# from django.shortcuts import render,redirect, HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProveedorForm
from .models import Proveedor

def proveedor_nuevo(request):
    if  request.method == 'POST':
        form = ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            proveedor=form.save()
            proveedor.save()
        return redirect('proveedor:listar_proveedor')
    else:
        form=ProveedorForm()


    return render(request, 'proveedor/proveedor_form.html',{'form':form})

def listar_productos(request):
	proveedor=Proveedor.objects.all()
	context={
			'proveedor':proveedor,
	}

	return render(request,'proveedor/proveedor_list.html',context)


 