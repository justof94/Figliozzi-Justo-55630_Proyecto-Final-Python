from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    username = forms.CharField(label="Usuario", max_length=50, disabled=True, required=False)
    email = forms.EmailField(label="Email", disabled=True, required=False)
    first_name = forms.CharField(label="Nombre", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido", max_length=50, required=False)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name', 'password1', 'password2']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)