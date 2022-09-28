from django.shortcuts import render
from rest_framework import viewsets
from cursos.models import Nota, Curso, Disciplina, Frequencia
from cursos.api.serializers import NotaSerializer, CursoSerializer, DisciplinaSerializer, FrequenciaSerializer

# Create your views here.

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

