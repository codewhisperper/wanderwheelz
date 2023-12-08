from django import forms
from .models import Car
from django.contrib.auth.forms import AuthenticationForm

class AdminLoginForm(AuthenticationForm):
    pass

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

