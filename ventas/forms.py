from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "w-full p-2 border rounded"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "w-full p-2 border rounded"}),
            "password1": forms.PasswordInput(attrs={"class": "w-full p-2 border rounded"}),
            "password2": forms.PasswordInput(attrs={"class": "w-full p-2 border rounded"}),
        }
