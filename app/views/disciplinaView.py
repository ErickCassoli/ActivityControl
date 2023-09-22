from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models.disciplina import Disciplina
from app.serializers.disciplinaSerializer import DisciplinaSerializer

# Classe com funções gerais (CREATE, GET ALL)
class DisciplinaView(APIView):

    # Esta função vai listar todas as disciplinas e retornar através do serializers
    def get(self, request):
        try:
            disciplinas = Disciplina.objects.all()
            serializer = DisciplinaSerializer(disciplinas, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Esta função vai criar uma nova disciplina através dos dados obtidos pelo serializers
    def post(self, request):
        try:
            serializer = DisciplinaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Classe com funções de disciplinas específicas
class DetailDisciplinaView(APIView):

    # Esta função vai puxar o objeto disciplina para fazer as outras funções relacionadas a um objeto específico
    def get_object(self, pk, entity):
        try:
            return entity.objects.get(pk=pk)
        except entity.DoesNotExist:
            raise Http404

    # Esta função vai listar uma disciplina específica.
    def get(self, request, pk, format=None):
        try:
            disciplina = self.get_object(pk, Disciplina)
            serializer = DisciplinaSerializer(disciplina)
            return Response(serializer.data)
        except Http404:
            return Response({'error': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Esta função vai atualizar uma disciplina específica de acordo com os dados obtidos no serializer
    def put(self, request, pk, format=None):
        try:
            disciplina = self.get_object(pk, Disciplina)
            serializer = DisciplinaSerializer(disciplina, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({'error': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Esta função vai deletar uma disciplina específica
    def delete(self, request, pk, format=None):
        try:
            disciplina = self.get_object(pk, Disciplina)
            disciplina.delete()
            return Response({'status': 'Disciplina deletada'},status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({'error': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
