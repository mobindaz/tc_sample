from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class CustomLoginForm(AuthenticationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)
