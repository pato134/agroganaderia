from django.shortcuts import render,redirect, HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
# Create your views here.
from .forms import ClienteForm, UserForm
from .models import Cliente
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.db import transaction

@transaction.atomic
def cliente_nuevo(request):
    cliente_form = ClienteForm()
    user_form = UserForm()

    context = {
            'cliente_form': cliente_form,
            'user_form': user_form,
    }
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        cliente_form = ClienteForm(request.POST)   
        if cliente_form.is_valid() and user_form.is_valid():
            # Validamos si cliente ya existe
            try:
                cedula_existe = Cliente.objects.get(cedula = cliente_form.cleaned_data['cedula'])
            except Cliente.DoesNotExist:
                cedula_existe = None
            if cedula_existe:
                messages.error(request, 'Cliente con esta cedula ya existe')
                return render(request, 'clientes/registro.html', context)

            user = user_form.save()
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            cliente = Cliente.objects.get(user = user)  
            # cliente_form.cleaned_data['user'] = user
            cliente.cedula = cliente_form.cleaned_data['cedula']
            cliente.direccion = cliente_form.cleaned_data['direccion']
            cliente.telefono = cliente_form.cleaned_data['telefono']
            cliente.genero = cliente_form.cleaned_data['genero']
            cliente.edad = cliente_form.cleaned_data['edad']
            cliente.lugar = cliente_form.cleaned_data['lugar']
            cliente.save()
            print(cliente)
            messages.success(request, 'Cliente creado correctamente!')
            return redirect('clientes:cliente_listar')

    return render(request, 'clientes/registro.html', context)





def cliente_listar(request):
    clientes=User.objects.all().select_related('cliente')
    print(clientes)
    context={
    		'object_list': clientes,



    }
    return render(request,'clientes/cliente_list.html',context)

def cliente_eliminar(request, id_cliente):
        obj_cliente = Cliente.objects.get(id=id_cliente)
        if request.method=="POST":
                obj_cliente.delete()
                return redirect('clientes:cliente_listar')

        return render(request, 'clientes/cliente_eliminar_form.html', {'cliente':obj_cliente})

def cliente_editar(request, id_cliente):
    cliente= Cliente.objects.get(id=id_cliente)
    if request.method=="POST":
          form = ClienteForm(request.POST, instance=cliente) 
          if form.is_valid():
            cliente= form.save()       
            return redirect('clientes:cliente_listar')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/cliente_editar_form.html',{'form': form})


def authentication(request):
    response= HttpResponseRedirect(request.GET.get('next'))
    print(response)
    cliente_form = ClienteForm()
    user_form = UserForm()
    context = {
            'cliente_form': cliente_form,
            'user_form': user_form,
            'next_url': response.url,
        }
    if request.method == 'POST':
        print("AUTENTICANDO")
        username  = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('producto:producto_listar')
        else:
            messages.error(request, 'Credenciales invalidas')
            context['mensaje'] = 'Credenciales invalidas'
            return render(request, 'login.html', context)

    else:
        print('usuario no autenticado')
        

        return render(request, 'clientes:login', context)
                
    return render(request, 'clientes:login', {})