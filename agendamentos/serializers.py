# agendamentos/serializers.py
from rest_framework import serializers
from .models import Agendamento, Historico

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'

class AgendamentoSerializer(serializers.ModelSerializer):
    historico = HistoricoSerializer(read_only=True)

    class Meta:
        model = Agendamento
        fields = '__all__'