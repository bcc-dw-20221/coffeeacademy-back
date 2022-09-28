from rest_framework.serializers import ModelSerializer
from gestao.models import Professor, Coordenador, Gestor

class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = ('__all__')

class CoordenadorSerializer(ModelSerializer):
    class Meta:
        model = Coordenador
        fields = ('__all__')

class GestorSerializer(ModelSerializer):
    class Meta:
        model = Gestor
        fields = ('__all__')