from django.shortcuts import render
from rest_framework import viewsets
from estudante.models import Alunos, Matricula, Pais, Egresso
from estudante.api.serializers import AlunosSerializer, MatriculaSerializer, PaisSerializer, EgressoSerializer

# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class EgressoViewSet(viewsets.ModelViewSet):
    queryset = Egresso.objects.all()
    serializer_class = EgressoSerializer

