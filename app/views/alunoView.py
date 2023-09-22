from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Aluno
from app.models.tarefa import Tarefa
from app.serializers.alunoSeriaizer import AlunoSerializer
from app.serializers.tarefaSerializer import TarefaSerializer

# Classe com funções gerais (CREATE, GET ALL)
class AlunoView(APIView):

    # Esta função vai listar todos os alunos e retornar através do serializers
    def get(self, request):
        try:
            alunos = Aluno.objects.all()
            serializer = AlunoSerializer(alunos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Esta função vai criar um novo aluno através dos dados obtidos pelo serializers
    def post(self, request):
        try:
            serializer = AlunoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Classe com funções de alunos específicos
class DetailAlunoView(APIView):

    # Esta função vai puxar o objeto aluno para fazer as outras funções relacionadas a um objeto específico
    def get_object(self, pk, entity):
        try:
            return entity.objects.get(pk=pk)
        except entity.DoesNotExist:
            raise Http404

    # Esta função vai listar um aluno específico.
    def get(self, request, pk, format=None):
        try:
            aluno = self.get_object(pk, Aluno)
            serializer = AlunoSerializer(aluno)
            return Response(serializer.data)
        except Http404:
            return Response({'error': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Esta função vai atualizar um aluno específico de acordo com os dados obtidos no serializer
    def put(self, request, pk, format=None):
        try:
            aluno = self.get_object(pk, Aluno)
            serializer = AlunoSerializer(aluno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({'error': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Esta função vai deletar um aluno específico
    def delete(self, request, pk, format=None):
        try:
            aluno = self.get_object(pk, Aluno)
            aluno.delete()
            return Response({'status': 'Aluno deletado'},status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({'error': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Classe com função para listar tarefa por aluno
class AlunoTarefaView(APIView):
    def get(self, request, aluno_id, format=None):
        try:
            tasks = Tarefa.objects.filter(aluno_id=aluno_id)
            serializer = TarefaSerializer(tasks, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
