from django import forms
from django.contrib.auth.models import User

from django.forms.extras import widgets
from django.contrib.admin import utils as admin_util
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import models as auth_models

# from material.frontend.account import metaforms
# from material.frontend.account import models
# from material.frontend.account import validators

from .models import Cliente


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
        }
        widgets = {
            'password':  forms.PasswordInput(),
        }


class ClienteForm(forms.ModelForm):

    class Meta:
        model= Cliente
        fields = ('cedula', 'direccion', 'lugar', 'telefono','genero','edad')

"""

# Example Django registration
class UserCreationForm(auth_forms.UserCreationForm):
  # This class defines creation form for `django.contrib.auth.models.User` objects.
  
  # It adds first name, last name and e-mail address fields and marks them as required. It validates hostname part of the e-mail
  # address and sets minimal length on username and password fields.
  
  error_css_class = 'error'
  required_css_class = 'required'
  fieldset = user_add_fieldsets

  class Meta(auth_forms.UserCreationForm.Meta):
    # By default first name, last name and e-mail address are not created at user creation, but we want them
    # user_add_fieldsets defines which fields we want at user creation
    fields = list(auth_forms.UserCreationForm.Meta.fields)
    for fieldset in user_add_fieldsets:
      fields.extend(fieldset[1]['fields'])
    
  def __init__(self, *args, **kwargs):
    super(UserCreationForm, self).__init__(*args, **kwargs)
    alter_user_form_fields(self)
    check_password_length(self)

  def clean_password2(self):
    # If password1 is invalid (and thus missing) we do not check password2 and let user first correct password1 error
    # There is a ticket about this: http://code.djangoproject.com/ticket/7833#comment:6
    if not self.cleaned_data.get('password1'):
      return self.cleaned_data.get('password2')
    return super(UserCreationForm, self).clean_password2()

  def clean_username(self):
    # Check for username existence in a case-insensitive manner
    username = super(UserCreationForm, self).clean_username()
    try:
      auth_models.User.objects.get(username__iexact=username)
    except auth_models.User.DoesNotExist:
      return username
    raise forms.ValidationError(_("A user with that username already exists."))


class UserProfileAndSettingsChangeForm(models.ModelForm):
  # This class defines change form for `frontend.account.models.UserProfileAndSettings` objects.

  error_css_class = 'error'
  required_css_class = 'required'

  class Meta:
    model = Cliente

class UserRegistrationForm(metaforms.FieldsetFormMixin, metaforms.ParentsIncludedModelFormMixin, UserCreationForm, UserProfileChangeForm):
    error_css_class = 'error'
    required_css_class = 'required'
    # fieldset = UserCreationForm.fieldset + [(
    # utils_text.capfirst(UserProfileChangeForm.Meta.model._meta.verbose_name), {
    #   'fields': UserProfileAndSettingsChangeForm.Meta.model.fieldset,
    # })]
    fieldset = UserCreationForm.fieldset + list(UserProfileAndSettingsChangeForm.Meta.model.fieldset)

    def save(self, commit=True):
        # We disable save method as registration backend module should take care of user and user
        # profile objects creation and we do not use this form for changing data
        assert False
        return None

    __metaclass__ = metaforms.ParentsIncludedModelFormMetaclass

"""