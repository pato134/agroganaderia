from django.forms import ModelForm

from django.contrib.admin import widgets
from django import forms

class ContactForm(forms.Form):
	nombre = forms.CharField(required=False)
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)