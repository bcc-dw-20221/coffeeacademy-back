from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from estudante.models import Alunos, Matricula, Pais, Egresso

class AlunosSerializer(ModelSerializer):
    nome = serializers.CharField(
        write_only = False,
        required = True,
        style = {'input_type': 'nome', 'placeholder':'nome'},
    )
    
    email = serializers.CharField(
        write_only = False,
        required = True,
        style = {'input_type': 'email', 'placeholder':'email'},
    )

    password = serializers.CharField(
        write_only = True,
        required = True,
        style = {'input_type': 'password', 'placeholder':'password'},
    )

    class Meta:
        model = Alunos
        fields = ('__all__')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(AlunosSerializer, self).create(validated_data)


class MatriculaSerializer(ModelSerializer):
    class Meta:
        model = Matricula
        fields = ('__all__')

class PaisSerializer(ModelSerializer):
    email = serializers.CharField(
        write_only = False,
        required = True,
        style = {'input_type': 'email', 'placeholder':'email'},
    )
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        style = {'input_type': 'password', 'placeholder':'password'},
    )

    class Meta:
        model = Pais
        fields = ('__all__')
        extra_kwargs = {'password':{'write_only': True}}
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(PaisSerializer, self).create(validated_data)


class EgressoSerializer(ModelSerializer):
    email = serializers.CharField(
        write_only = False,
        required = True,
        style = {'input_type': 'email', 'placeholder':'email'},
    )
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        style = {'input_type': 'password', 'placeholder':'password'},
    )
    
    class Meta:
        model = Egresso
        fields = ('__all__')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(EgressoSerializer, self).create(validated_data)
    
