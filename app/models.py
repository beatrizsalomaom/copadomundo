# Create your models here.
from django.db import models

class Equipe(models.Model):
    nomeequipe = models.CharField(max_length=20, verbose_name="Seleção")
    continente = models.CharField(max_length=20, verbose_name="Continente")
    nometecnico = models.CharField(max_length=50, verbose_name="Técnico")
    grupo = models.CharField(max_length=1, verbose_name="Grupo")
    def __str__(self):
        return f"{self.nomeequipe}, {self.continente}, {self.nometecnico}, {self.grupo}"
    class Meta:
        verbose_name = "Seleção"
        verbose_name_plural = "Seleções"


class Jogador(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do jogador")
    clube = models.CharField(max_length=20, verbose_name="Clube")
    posicao = models.CharField(max_length=20, verbose_name="Posição")
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.equipe.nomeequipe})"
    class Meta:
        verbose_name = "Jogador"
        verbose_name_plural = "Jogadores"


class Estadio(models.Model):
    estadio = models.CharField(max_length=50, verbose_name="Nome do Estádio")
    cidade = models.CharField(max_length=20, verbose_name="Cidade")
    UF = models.CharField(max_length=5, verbose_name="UF")
    capacidade = models.IntegerField(verbose_name="Capacidade")

    def __str__(self):
        return f"{self.estadio}, {self.cidade}, {self.UF}, {self.capacidade}"
    class Meta:
        verbose_name = "Estádio"
        verbose_name_plural = "Estádios"


class Partida(models.Model):
    mandante = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='mandante')
    visitante = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='visitante')
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    data = models.DateTimeField()
    gols_mandante = models.IntegerField(default=0)
    gols_visitante = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.mandante.nomeequipe} x {self.visitante.nomeequipe}"


class Gol(models.Model):
    partida = models.ForeignKey(
        Partida, on_delete=models.CASCADE, related_name="gols"
    )
    jogador = models.ForeignKey(
        Jogador, on_delete=models.CASCADE, related_name="gols"
    )
    minuto = models.IntegerField()

    def __str__(self):
        return f"Gol de {self.jogador.nome} aos {self.minuto}'"
