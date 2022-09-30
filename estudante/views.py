from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.core import serializers

from django.contrib.auth import get_user_model

from django.views.decorators.http import require_http_methods

from estudante.models import Alunos

require_http_methods(["GET"])
def get_alunos(request):
    """Retorna todas as postagens."""
    alunos = Alunos.objects.all()

    resp_json = serializers.serialize("json", alunos)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["GET"])
def get_alunos_matricula(request, matricula):
    """Retorna todas as postagens."""
    alunos = Alunos.objects.filter(pk=matricula)

    resp_json = serializers.serialize("json", alunos)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["POST"])
def post_alunos(request):
    """Adiciona um post."""
    novo = Alunos()
    novo.nome = request.POST["nome"]
    novo.matricula = get_user_model().objects.get(pk=request.POST["matricula"])
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
    #novo.curso = request.POST["curso"]
    #novo.disciplinas = request.POST["disciplinas"]
    #novo.pais = request.POST["pais"]
    novo.save()
    return HttpResponse("Aluno criado com Sucesso!")

@require_http_methods(["DELETE"])
def delete_aluno(request, matricula):
    post = Alunos.objects.get(pk=matricula)
    post.delete()

    return HttpResponse("Aluno Deletado com sucesso.")
