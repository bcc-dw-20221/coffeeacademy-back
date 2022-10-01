# Create your views here.
from django.shortcuts import HttpResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods

from cursos.models import Curso, Nota, Disciplina, Frequencia
z
# View da Classe CURSO
@require_http_methods(["GET"])
def get_cursos(request):
    """Retorna todos os cursos"""
    cursos = Curso.objects.all()

    resp_json = serializers.serialize("json", cursos)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["GET"])
def get_curso(request, curso_id):
    """Retorna apenas um curso."""
    curso = Curso.objects.filter(pk=curso_id)

    curso_json = serializers.serialize("json", curso)

    return HttpResponse(curso_json, content_type="application/json")


@require_http_methods(["POST"])
def post_curso(request):
    """Adiciona um curso."""
    novo_curso = Curso()
    novo_curso.nome_curso = request.POST["nome_curso"]
    # lista de disciplinas -> implementar
    novo_curso.quantidade_vagas = request.POST["quantidade_vagas"]
    novo_curso.save()
    return HttpResponse("Curso adicionado!")


@require_http_methods(["DELETE"])
def delete_curso(request, curso_id):
    """Deletar um curso"""
    curso = Curso.objects.get(pk=curso_id)
    curso.delete()

    return HttpResponse("Deletado com sucesso.")

# View da Classe NOTA
@require_http_methods(["GET"])
def get_notas(request):
    """Retorna todas as notas"""
    notas = Nota.objects.all()

    resp_json = serializers.serialize("json", notas)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["GET"])
def get_nota(request, nota_id):
    """Retorna apenas uma nota."""
    nota = Nota.objects.filter(pk=nota_id)

    nota_json = serializers.serialize("json", nota)

    return HttpResponse(notas_json, content_type="application/json")


@require_http_methods(["POST"])
def post_nota(request):
    """Adiciona uma nota."""
    nova_nota = Nota()
    # disciplina -> implementar
    nova_nota.nota_disciplina = request.POST["nota_disciplina"]  
    nova_nota.save()
    return HttpResponse("Nota adicionada!")


@require_http_methods(["DELETE"])
def delete_curso(request, nota_id):
    """Deletar um nota"""
    nota = Nota.objects.get(pk=nota_id)
    nota.delete()

    return HttpResponse("Deletado com sucesso.")

# View da Classe DISCIPLINA
@require_http_methods(["GET"])
def get_disciplinas(request):
    """Retorna todas as disciplinas."""
    disciplinas = Disciplina.objects.all()

    resp_json = serializers.serialize("json", disciplinas)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["GET"])
def get_disciplina(request, disciplina_id):
    """Retorna apenas uma nota."""
    disciplina = Disciplina.objects.filter(pk=disciplina_id)

    disciplina_json = serializers.serialize("json", disciplina)

    return HttpResponse(disciplina_json, content_type="application/json")


@require_http_methods(["POST"])
def post_disciplina(request):
    """Adiciona uma disciplina."""
    nova_disciplina = Disciplina()
    # id_disciplina -> implementar
    nova_disciplina.nome_disciplina= request.POST["nome_disciplina"] 
    # alunos(lista) -> implementar
    # curso -> implementar
    # professor -> implementar
    # semestre -> implementar
    nova_disciplina.quantidade_vagas = request.POST["quantidade_vagas"]
    nova_disciplina.quantidade_creditos = request.POST["quantidade_creditos"]
    nova_disciplina.tipo_disciplina = request.POST["tipo_disciplina"]
    # dia_aula -> implementar
    # hora_aula -> implementar
    nova_disciplina.carga_horaria = request.POST["carga_horaria"]
    nova_disciplina.conteudo_ministrado = request.POST["conteudo_ministrado"]
    # material_disciplina -> implementar
    nova_disciplina.save()
    return HttpResponse("Disciplina adicionada!")


@require_http_methods(["DELETE"])
def delete_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    disciplina.delete()

    return HttpResponse("Deletado com sucesso.")

# View da Classe FREQUENCIA
@require_http_methods(["GET"])
def get_frequencias(request):
    """Retorna todas as frequencias."""
    frequencias = Frequencia.objects.all()

    resp_json = serializers.serialize("json", frequencias)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["GET"])
def get_frequencia(request, frequencia_id):
    """Retorna apenas uma frequencia."""
    frequencia = Frequencia.objects.filter(pk=frequencia_id)

    frequencia_json = serializers.serialize("json", frequencia)

    return HttpResponse(frequencia_json, content_type="application/json")


@require_http_methods(["POST"])
def post_frequencia(request):
    """Adiciona uma frequencia."""
    nova_frequencia = Frequencia()
    # id_disciplina -> implementar
    nova_frequencia.data_aula= request.POST["data_aula"] 
    nova_frequencia.titulo_dias_aula - request.POST["titulo_dias_aula"]
    nova_frequencia.save()
    return HttpResponse("Frequencia adicionada!")


@require_http_methods(["DELETE"])
def delete_frequencia(request, frequencia_id):
    frequencia = Frequencia.objects.get(pk=frequencia_id)
    frequencia.delete()

    return HttpResponse("Deletado com sucesso.")




