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
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "otroemail@gmail.com"]
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
