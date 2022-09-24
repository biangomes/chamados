from django.forms import ModelForm, forms
import os
from django.core.exceptions import ValidationError
from django import forms
from chamados.models import Chamado, Analise



# Form responsável por cadastrar o chamado
class ChamadoForm(forms.ModelForm):
    # sccd = forms.IntegerField(min_value=000000, max_value=999999, label='SCCD')
    # titulo = forms.CharField(max_length=200, label='Titulo do chamado')
    # descricao = forms.CharField(null=True)
    class Meta:
        model = Chamado
        fields = ['sccd', 'titulo', 'descricao', 'cliente', 'severidade']
