from django import forms

class Personas(forms.Form):
    nombre = forms.CharField(max_length=100, blank=True, null=True)
    apellido = forms.CharField(max_length=100, blank=True, null=True)
    email = forms.CharField(unique=True, max_length=255, blank=True, null=True)