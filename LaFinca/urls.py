from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login
#from django.views.i18n import JavaScriptCatalog

urlpatterns = [
	  url(r'^', include('home.urls', namespace='home')),
    url(r'^admin/', admin.site.urls),
    url(r'^galeria/', include('galeria.urls', namespace='galeria')),
    url(r'^productos/', include('productos.urls', namespace='productos')),
    url(r'^contactos/', include('contactos.urls', namespace='contactos')),
    url(r'^quienessomos/', include('quienessomos.urls', namespace='quienessomos')),
    url(r'^clientes/', include('clientes.urls', namespace='clientes')),
    url(r'^usuario/', include('usuario.urls', namespace='usuario')),
    url(r'^facturas/', include('facturas.urls', namespace='facturas')),
    # url(r'^proveedor/', include('proveedor.urls', namespace='proveedor')),
   	

   # url(r'', include('.urls', namespace='Agroganaderia')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
if settings.DEBUG:
		urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
