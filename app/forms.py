from django import forms
from .models import Gol

class GolForm(forms.ModelForm):
    class Meta:
        model = Gol
        fields = ['partida', 'jogador', 'minuto']
