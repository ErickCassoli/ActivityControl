from django.urls import path
from app.views.alunoView import AlunoView, DetailAlunoView, AlunoTarefaView
from app.views.disciplinaView import DisciplinaView, DetailDisciplinaView
from app.views.tarefaView import TarefaView, DetailTarefaView

urlpatterns = [
    # Rotas para Alunos
    path('api/alunos/', AlunoView.as_view(), name='lista_ou_cria_alunos'),
    path('api/alunos/<int:pk>/', DetailAlunoView.as_view(), name='detalhes_aluno'),
    path('api/alunos/<aluno_id>/tarefas/', AlunoTarefaView.as_view(), name='tarefas_aluno'),

    # Rotas para Disciplinas
    path('api/disciplinas/', DisciplinaView.as_view(), name='lista_ou_cria_disciplinas'),
    path('api/disciplinas/<int:pk>/', DetailDisciplinaView.as_view(), name='detalhes_disciplina'),

    # Rotas para Tarefas
    path('api/tarefas/', TarefaView.as_view(), name='lista_tarefas'),
    path('api/tarefas/<int:pk>/', DetailTarefaView.as_view(), name='detalhes_tarefa'),
]
