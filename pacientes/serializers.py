# pacientes/serializers.py
from rest_framework import serializers
from .models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

    def validate_cpf(self, value):
        # Remove formatação
        cpf = value.replace('.', '').replace('-', '')
        if len(cpf) != 11:
            raise serializers.ValidationError("CPF inválido.")
        return value