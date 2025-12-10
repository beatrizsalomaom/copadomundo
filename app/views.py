from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


def listar_equipes_por_grupo(request):
    grupos = {}
    for letra in "ABCDEFGH":  # Copa tem 8 grupos
        grupos[letra] = Equipe.objects.filter(grupo=letra).order_by("nomeequipe")

    return render(request, "equipe.html", {"grupos": grupos})


class JogadorView(View):
    def get(self, request, *args, **kwargs):
        jogador = Jogador.objects.all()
        return render(request, 'jogador.html', {'jogador': jogador})


class EstadiosView(View):
    def get(self, request, *args, **kwargs):
        estadio = Estadio.objects.all()
        return render(request, 'estadio.html', {'estadio': estadio})


class PartidasView(View):
    def get(self, request, *args, **kwargs):
        partidas = Partida.objects.select_related(
            "mandante", "visitante", "estadio"
        ).all()

        return render(request, 'partida.html', {'partidas': partidas})


class GolssView(View):
    def get(self, request, *args, **kwargs):
        gol = Gol.objects.all()
        return render(request, 'gol.html', {'gol': gol})
