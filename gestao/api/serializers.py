from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from gestao.models import Professor, Coordenador, Gestor
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password


class ProfessorSerializer(ModelSerializer):
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
        model = Professor
        fields = ('__all__')
        extra_kwargs = {'password':{'write_only': True}}
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(ProfessorSerializer, self).create(validated_data)


class CoordenadorSerializer(ModelSerializer):
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
        model = Coordenador
        fields = ('__all__')
        extra_kwargs = {'password':{'write_only': True}}
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(CoordenadorSerializer, self).create(validated_data)


class GestorSerializer(ModelSerializer):
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
        model = Gestor
        fields = ('__all__')
        extra_kwargs = {'password':{'write_only': True}}
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(GestorSerializer, self).create(validated_data)

