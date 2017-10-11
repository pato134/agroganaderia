from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Cliente

class UsuarioCreationForm(UserCreationForm):
    # def _init_(self, *args, **kargs):
    #   super(ClienteCreationForm, self)._init_(*args, **kargs)
    #   del self.fields['username']

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

class CLienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        