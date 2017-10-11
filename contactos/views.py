from django.shortcuts import render

def contactos_nuevo(request):
	return render(request, 'contactos.html',{})
