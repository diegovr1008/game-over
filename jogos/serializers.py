from datetime import date
from rest_framework import serializers
from .models import Jogo

# (Lacuna 1): O ModelSerializer cria os campos automaticamente olhando para o model.
class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        # (Lacuna 2): Informamos que o model base é o Jogo.
        model = Jogo
        fields = ['id', 'titulo', 'genero', 'plataforma', 'ano_lancamento', 'preco', 'disponivel']
        
        # (Lacuna 3): Bloqueia o envio do id na criação, pois quem o gera é a base de dados.
        read_only_fields = ['id']

    # (Lacuna 4): validate_ano_lancamento segue o padrão de validação do DRF.
    def validate_ano_lancamento(self, valor):
        if valor > date.today().year:
            # (Lacuna 5): Levanta um erro de validação do DRF.
            raise serializers.ValidationError("O ano não pode estar no futuro.")
        return valor

    # (Lacuna 6): Regra de negócio criada do zero para validar o preço.
    def validate_preco(self, valor):
        if valor < 0:
            raise serializers.ValidationError("O preço não pode ser negativo.")
        return valor