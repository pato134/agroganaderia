from django.conf.urls import url , include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [


	url(r'^registro/$', views.cliente_nuevo, name='registro'),
	url(r'^login/$', views.authentication, name='login'),
	url(r'^logout$', auth_views.logout, {'next_page': 'home:index'}, name='logout'),
	url(r'^listar/$', views.cliente_listar, name='cliente_listar'),
	url(r'^eliminar/(?P<id_cliente>\d+)$', views.cliente_eliminar, name='cliente_eliminar'),
	url(r'^editar/(?P<id_cliente>\d+)$', views.cliente_editar, name='cliente_editar'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls'))
	
	


	

]