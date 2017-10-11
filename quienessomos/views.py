from django.shortcuts import render

def listar_quienessomos(request):
	return render(request,'quienessomos.html',{})
