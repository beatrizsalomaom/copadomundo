from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView, JogadorView, EstadiosView, PartidasView, GolssView,
    listar_equipes_por_grupo, deletar_gol
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path("equipe/", listar_equipes_por_grupo, name="equipe"),
    path('jogador/', JogadorView.as_view(), name='jogador'),
    path('estadio/', EstadiosView.as_view(), name='estadio'),
    path('partida/', PartidasView.as_view(), name='partida'),
    path('gol/', GolssView.as_view(), name='gol'),
    path('gol/deletar/<int:gol_id>/', deletar_gol, name='deletar_gol'),

]
