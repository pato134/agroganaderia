# # from django.shortcuts import render,redirect, HttpResponseRedirect
# from django import forms
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from django.utils.translation import ugettext as _
# # Create your views here.
# from .forms import ProveedorForm, UserForm
# from .models import Proveedor
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy


# def proveedor_nuevo(request):
#     if request.method == 'POST':
#         proveedor_form = ProveedorForm(request.POST)   
#         if proveedor_form.is_valid() and user_form.is_valid():
#             proveedor = Proveedor.objects.get(user = user)  
#             print(proveedor)
#             # cliente_form.cleaned_data['user'] = user
#             proveedor.cedula =proveedor_form.cleaned_data['cedula']
#             proveedor.telefono = proveedor_form.cleaned_data['telefono']
#             proveedor.direccion = proveedor_form.cleaned_data['direccion']
#             proveedor.nombre_empresa = proveedor_form.cleaned_data['nombre_empresa']
#             proveedor.direccion_empresa = proveedor_form.cleaned_data['direccion_empresa']
#             proveedor.telefono_empresa = proveedor_form.cleaned_data['telefono_empresa']
#             proveedor.save()
#             print(proveedor)
#             messages.success(request, _('Proveedor creado correctamente!'))
#             return redirect('proveedor:proveedor_listar')
#     else:
#         proveedor_form = ProveedorForm()
#         user_form = UserForm()

#     context = {
#             'proveedor_form': proveedor_form,
#     }

#     return render(request, 'proveedor/registro.html', context)





# def proveedor_listar(request):
#     proveedores=User.objects.all().select_related('cliente')
#     print(proveedores)
#     context={
#     		'object_list': proveedores,



#     }
#     return render(request,'provedor/proveedor_list.html',context)

# def proveedor_eliminar(request, id_proveedor):
#         obj_proveedor = proveedor.objects.get(id=id_proveedor)
#         if request.method=="POST":
#                 obj_proveedor.delete()
#                 return redirect('proveedor:proveedor_listar')

#         return render(request, 'proveedores/proveedor_eliminar_form.html', {'proveedor':obj_proveedor})

# def proveedor_editar(request, id_cliente):
#     proveedor= Proveedor.objects.get(id=id_proveedor)
#     if request.method=="POST":
#           form = ProveedorForm(request.POST, instance=proveedor) 
#           if form.is_valid():
#             proveedor= form.save()       
#             return redirect('proveedor:proveedor_listar')
#     else:
#         form = ProveedorForm(instance=proveedor)

#     return render(request, 'Proveedor/proveedor_editar_form.html',{'form': form})


# def authentication(request):
#     response= HttpResponseRedirect(request.GET.get('next'))
#     print(response)
#     proveedor_form = ProveedorForm()
#     user_form = UserForm()
#     context = {
#             'proveedor_form': proveedor_form,
#             'user_form': user_form,
#             'next_url': response.url,
#         }
#     if request.method == 'POST':
#         print("AUTENTICANDO")
#         username  = request.POST.get('username', None)
#         password = request.POST.get('password', None)

#         user = authenticate(username = username, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect('producto:producto_listar')
#         else:
#             messages.error(request, 'Credenciales invalidas')
#             return render(request, 'proveedor/login.html', context)

#     else:
#         print('usuario no autenticado')
        

#         return render(request, 'proveedor/login.html', context)
                
#     return render(request, 'proveedor:login', {})