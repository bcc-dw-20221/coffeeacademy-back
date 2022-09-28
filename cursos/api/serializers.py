from rest_framework.serializers import ModelSerializer
from cursos.models import Nota, Curso, Disciplina, Frequencia

class NotaSerializer(ModelSerializer):
    class Meta:
        model = Nota
        fields = ('__all__')

class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = ('__all__')

class DisciplinaSerializer(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ('__all__')

class FrequenciaSerializer(ModelSerializer):
    class Meta:
        model = Frequencia
        fields = ('__all__')