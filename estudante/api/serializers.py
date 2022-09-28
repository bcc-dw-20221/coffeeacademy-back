from rest_framework.serializers import ModelSerializer
from estudante.models import Alunos, Matricula, Pais, Egresso

class AlunosSerializer(ModelSerializer):
    class Meta:
        model = Alunos
        fields = ('__all__')

class MatriculaSerializer(ModelSerializer):
    class Meta:
        model = Matricula
        fields = ('__all__')

class PaisSerializer(ModelSerializer):
    class Meta:
        model = Pais
        fields = ('__all__')

class EgressoSerializer(ModelSerializer):
    class Meta:
        model = Egresso
        fields = ('__all__')