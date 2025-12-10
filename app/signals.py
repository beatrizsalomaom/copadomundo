from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Gol, Partida

@receiver(post_save, sender=Gol)
def atualizar_gols_partida(sender, instance, created, **kwargs):
    if created:  # só atualiza quando o gol é criado
        partida = instance.partida
        jogador = instance.jogador

        # Verifica se o gol é do mandante ou visitante
        if jogador.equipe == partida.mandante:
            partida.gols_mandante += 1
        elif jogador.equipe == partida.visitante:
            partida.gols_visitante += 1

        partida.save()
