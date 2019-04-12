from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserCreationFormWithEmail(UserCreationForm):
   email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")
   
   class Meta:
      model = User
      fields = ['username','email', 'password1','password2']

   def clean_email(self):
      # Recuperamos el email que estamos ingresando
      email = self.cleaned_data.get('email')
      # Comprobamos si existe algun usuario con este email
      if User.objects.filter(email=email).exists():
         # Invocamos un error de validación
         raise forms.ValidationError('El email ya esta registrado prueba con otro')
      return email

class ProfileForm(ModelForm):
      
   class Meta:
      model = Profile
      fields = ['avatar','bio','link']
      widgets = {
         'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3', 'placeholder':'Retrato'}),
         'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows': 3, 'placeholder':'Biografía'}),
         'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'})
      }

class EmailForm(ModelForm):
   email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")
    
   class Meta:
      model = User
      fields = ("email",)

   def clean_email(self):
      # Recuperamos el email que estamos ingresando
      email = self.cleaned_data.get('email')
      if 'email' in self.changed_data:
         # Comprobamos si existe algun usuario con este email
         if User.objects.filter(email=email).exists():
            # Invocamos un error de validación
            raise forms.ValidationError('El email ya esta registrado prueba con otro')
      return email