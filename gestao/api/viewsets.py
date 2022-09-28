from django.shortcuts import render
from rest_framework import viewsets
from gestao.models import Professor, Coordenador, Gestor
from gestao.api.serializers import ProfessorSerializer, CoordenadorSerializer, GestorSerializer

# Create your views here.

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class CoordenadorViewSet(viewsets.ModelViewSet):
    queryset = Coordenador.objects.all()
    serializer_class = CoordenadorSerializer

class GestorViewSet(viewsets.ModelViewSet):
    queryset = Gestor.objects.all()
    serializer_class = GestorSerializer