from rest_framework import viewsets
from .models import Jogo
from .serializers import JogoSerializer

# (Lacuna 7): O ModelViewSet é a classe que já traz as seis ações prontas (list, retrieve, create, update, partial_update e destroy).
class JogoViewSet(viewsets.ModelViewSet):
    # (Lacuna 8): O queryset diz à view onde ela deve ir buscar os dados na base de dados (ordenados pelo título).
    queryset = Jogo.objects.all().order_by('titulo')
    
    # (Lacuna 9): O serializer_class indica qual tradutor/fiscal usar para estes dados.
    serializer_class = JogoSerializer