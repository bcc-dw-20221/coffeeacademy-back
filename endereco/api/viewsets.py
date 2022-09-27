from django.shortcuts import render
from rest_framework import viewsets
from endereco.models import Endereco
from .serializers import EnderecoSerializer

# Create your views here.

class EnderecoViewSet(viewsets.ViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer