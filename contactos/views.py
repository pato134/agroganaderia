from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
def contactos_nuevo(request):
	titulo = "Contacto"
	formulario = ContactForm(request.POST or None)
	if formulario.is_valid():

		form_email = formulario.cleaned_data.get("email")
		form_mensaje = formulario.cleaned_data.get("mensaje")
		form_nombre = formulario.cleaned_data.get("nombre")
		asunto = 'Form de Contacto'
		email_from = 'espinosap430@gmail.com'
		email_to = [email_from, form_email]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)

			# print email, mensaje, nombre
	context = {
		"formulario": formulario,
		"titulo": titulo,
	}
	return render(request, 'contactos.html',context)
