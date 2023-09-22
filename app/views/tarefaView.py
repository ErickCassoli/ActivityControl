from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Tarefa
from app.serializers.tarefaSerializer import TarefaSerializer

# Classe com funções gerais (CREATE, GET ALL)
class TarefaView(APIView):

    # Esta função vai listar todas as tarefas e retornar através do serializers
    def get(self, request):
        try:
            tarefas = Tarefa.objects.all()
            serializer = TarefaSerializer(tarefas, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Esta função vai criar uma nova tarefa através dos dados obtidos pelo serializers
    def post(self, request):
        try:
            serializer = TarefaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Classe com funções de tarefas específicas
class DetailTarefaView(APIView):

    # Esta função vai puxar o objeto tarefa para fazer as outras funções relacionadas a um objeto específico
    def get_object(self, pk, entity):
        try:
            return entity.objects.get(pk=pk)
        except entity.DoesNotExist:
            raise Http404

    # Esta função vai listar uma tarefa específica.
    def get(self, request, pk, format=None):
        try:
            tarefa = self.get_object(pk, Tarefa)
            serializer = TarefaSerializer(tarefa)
            return Response(serializer.data)
        except Http404:
            return Response({'error': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Esta função vai atualizar uma tarefa específica de acordo com os dados obtidos no serializer
    def put(self, request, pk, format=None):
        try:
            tarefa = self.get_object(pk, Tarefa)
            serializer = TarefaSerializer(tarefa, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({'error': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Esta função vai deletar uma tarefa específica
    def delete(self, request, pk, format=None):
        try:
            tarefa = self.get_object(pk, Tarefa)
            tarefa.delete()
            return Response({'status': 'Tarefa deletada'},status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({'error': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
