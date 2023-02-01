from django import forms
from .models import *

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ('titulo','nome', 'posologia', 'quantidade', 'via')
        widgets = {
          'titulo': forms.TextInput(
                attrs={'type': 'text', 'nome': 'titulo', 'placeholder': 'Titulo'}),
            'nome': forms.TextInput(
                attrs={'type': 'text', 'nome': 'nome', 'placeholder': 'Nome / Dosagem'}),
            'posologia': forms.TextInput(
                attrs={'type': 'text', 'nome': 'posologia', 'placeholder': 'Posologia'}),
            'quantidade': forms.TextInput(
                attrs={'type': 'text', 'nome': 'quantidade', 'placeholder': 'Quantidade'}),                
            'via': forms.Select(
                attrs={'nome': 'via'}),
        }