from django import forms
class Formulario_Persona(forms.Form):
    nombre = forms.CharField(max_length=100, label="Ingresa tu nombre")
    apellidos = forms.CharField(max_length=100, label="Apellidos")


