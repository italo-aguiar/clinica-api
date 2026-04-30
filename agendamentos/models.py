# agendamentos/models.py
from django.db import models
from pacientes.models import Paciente

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('agendado', 'Agendado'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('realizado', 'Realizado'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='agendamentos')
    data_hora = models.DateTimeField()
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='agendado')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paciente.nome} - {self.data_hora}"


class Historico(models.Model):
    agendamento = models.OneToOneField(Agendamento, on_delete=models.CASCADE)
    observacoes = models.TextField()
    prescricao = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)