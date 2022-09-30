from django.shortcuts import render

# Create your views here.
"""Views do bar."""

# Create your views here.
from django.shortcuts import HttpResponse
from django.core import serializers

from django.contrib.auth import get_user_model

from django.views.decorators.http import require_http_methods

from gestao.models import Professor, Coordenador, Gestor


'''
views Professor
'''
@require_http_methods(["GET"])
def get_professor(request):
    """Retorna todos os professores."""
    professor = Professor.objects.all()

    resp_json = serializers.serialize("json", professor)

    return HttpResponse(resp_json, content_type="application/json")


@require_http_methods(["GET"])
def get_professor_id(request, professor_id):
    """Retorna um professor."""
    professor = Professor.objects.filter(pk=professor_id)

    professor_json = serializers.serialize("json", professor)

    return HttpResponse(professor_json, content_type="application/json")


@require_http_methods(["POST"])
def post_professor(request):
    """Adiciona um professor."""
    novo = Professor()
    novo.nome = request.POST["nome"]
    novo.email = request.POST["email"]
    novo.password = novo.set_password(request.POST["password"])
    novo.telefone = request.POST["telefone"]
    novo.cpf = request.POST["cpf"]
    novo.rg = request.POST["rg"]
    novo.data_nascimento = request.POST["data_nascimento"]
    novo.sexo = request.POST["sexo"]
    novo.estado_civil = request.POST["estado_civil"]
    novo.naturalidade = request.POST["naturalidade"]
    novo.endereco = request.POST["endereco"]
    novo.curso = request.POST["curso"]
    novo.carga_horaria = request.POST["carga_horaria"]
    novo.save()
    return HttpResponse("professor criado com sucesso")


@require_http_methods(["GET"])
def delete_professor(request, professor_id):
    """Deleta um professor"""
    professor = Professor.objects.get(pk=professor_id)
    professor.delete()

    return HttpResponse("Deletado com sucesso.")


'''
views Coordenador
'''
@require_http_methods(["GET"])
def get_coordenador(request):
    """Retorna todos os coordenadores."""
    coordenador = Coordenador.objects.all()

    resp_json = serializers.serialize("json", coordenador)

    return HttpResponse(resp_json, content_type="application/json")


@require_http_methods(["GET"])
def get_coordenador_id(request, coordenador_id):
    """Retorna um coordenador."""
    coordenador = Coordenador.objects.filter(pk=coordenador_id)

    coordenador_json = serializers.serialize("json", coordenador)

    return HttpResponse(coordenador_json, content_type="application/json")


@require_http_methods(["POST"])
def post_coordenador(request):
    """Adiciona um coordenador."""
    novo = Coordenador()
    novo.nome = request.POST["nome"]
    novo.email = request.POST["email"]
    novo.password = novo.set_password(request.POST["password"])
    novo.telefone = request.POST["telefone"]
    novo.cpf = request.POST["cpf"]
    novo.rg = request.POST["rg"]
    novo.data_nascimento = request.POST["data_nascimento"]
    novo.sexo = request.POST["sexo"]
    novo.estado_civil = request.POST["estado_civil"]
    novo.naturalidade = request.POST["naturalidade"]
    novo.endereco = request.POST["endereco"]
    novo.save()
    return HttpResponse("coordenador criado com sucesso")


@require_http_methods(["DELETE"])
def delete_coordenador(request, coordenador_id):
    coordenador = Coordenador.objects.get(pk=coordenador_id)
    coordenador.delete()

    return HttpResponse("Deletado com sucesso.")

'''
views Gestor
'''
@require_http_methods(["GET"])
def get_gestor(request):
    """Retorna todos os gestores."""
    gestor = Gestor.objects.all()

    resp_json = serializers.serialize("json", gestor)

    return HttpResponse(resp_json, content_type="application/json")


@require_http_methods(["GET"])
def get_gestor_id(request, gestor_id):
    """Retorna um gestor."""
    gestor = Gestor.objects.filter(pk=gestor_id)

    gestor_json = serializers.serialize("json", gestor)

    return HttpResponse(gestor_json, content_type="application/json")


@require_http_methods(["POST"])
def post_gestor(request):
    """Adiciona um gestor."""
    novo = Gestor()
    novo.nome = request.POST["nome"]
    novo.email = request.POST["email"]
    novo.password = novo.set_password(request.POST["password"])
    novo.telefone = request.POST["telefone"]
    novo.cpf = request.POST["cpf"]
    novo.rg = request.POST["rg"]
    novo.data_nascimento = request.POST["data_nascimento"]
    novo.sexo = request.POST["sexo"]
    novo.estado_civil = request.POST["estado_civil"]
    novo.naturalidade = request.POST["naturalidade"]
    novo.endereco = request.POST["endereco"]
    novo.save()
    return HttpResponse("gestor criado com sucesso")


@require_http_methods(["DELETE"])
def delete_gestor(request, gestor_id):
    gestor = Gestor.objects.get(pk=gestor_id)
    gestor.delete()

    return HttpResponse("Deletado com sucesso.")