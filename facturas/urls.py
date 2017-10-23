from django.conf.urls import url, include
from . import views

urlpatterns = [
	#url(r'^$', views.mostrar_inicio),
	
    url(r'^nueva/$', views.factura_nuevo, name='factura_crear'),
]