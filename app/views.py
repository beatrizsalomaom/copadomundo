from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import GolForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


def listar_equipes_por_grupo(request):
    grupos = {}
    for letra in "ABCDEFGH":
        grupos[letra] = Equipe.objects.filter(grupo=letra).order_by("nomeequipe")
    return render(request, "equipe.html", {"grupos": grupos})


class JogadorView(View):
    def get(self, request):
        equipes = Equipe.objects.all().order_by("nomeequipe").prefetch_related("jogador_set")
        return render(request, "jogador.html", {"equipes": equipes})



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
    def get(self, request):
        gols = Gol.objects.all().order_by("partida")
        form = GolForm()
        return render(request, "gol.html", {"gols": gols, "form": form})

    def post(self, request):
        form = GolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/gol/")
        else:
            gols = Gol.objects.all()
            return render(request, "gol.html", {"gols": gols, "form": form})


def deletar_gol(request, gol_id):
    gol = get_object_or_404(Gol, id=gol_id)
    gol.delete()
    return redirect("/gol/")
