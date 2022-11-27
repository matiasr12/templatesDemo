from django import forms
from templatesApp.models import Trabajadores

class FormTrabajadores(forms.ModelForm):
    class Meta:
        model=Trabajadores
        fields='__all__'