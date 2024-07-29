from django import forms
from .models import Pedido
from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome', 'email', 'tipo_hamburguer', 'valor_total']