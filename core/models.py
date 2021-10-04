from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:                             # altera o nome da tabela de Coreevento para evento
        db_table = 'evento'

    def __str__(self):                      # altera o object no adminn para Evento
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y  --   %H:%M h')