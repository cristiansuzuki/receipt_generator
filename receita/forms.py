from django import forms
from .models import *

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ('titulo','nome', 'posologia', 'via')
        widgets = {
          'titulo': forms.TextInput(
                attrs={'type': 'text', 'nome': 'titulo', 'placeholder': 'Titulo'}),
            'nome': forms.TextInput(
                attrs={'type': 'text', 'nome': 'nome', 'placeholder': 'Nome / Dosagem'}),
            'posologia': forms.TextInput(
                attrs={'type': 'text', 'nome': 'posologia', 'placeholder': 'Posologia'}),
            'via': forms.Select(
                attrs={'nome': 'via'}),
        }