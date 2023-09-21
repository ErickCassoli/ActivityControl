from django.db import models
from .aluno import Aluno
from .disciplina import Disciplina

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_entrega = models.DateField()
    concluida = models.BooleanField(default=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.titulo
