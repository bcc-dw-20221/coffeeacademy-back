from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.core import serializers

from django.contrib.auth import get_user_model, login, logout

from django.views.decorators.http import require_http_methods

from estudante.models import Alunos, Matricula, Pais, Egresso

from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import permission_required

from django.core.exceptions import ObjectDoesNotExist

""" views do Aluno"""
@require_http_methods(["GET","POST"])
def login_alunos(request):
    ''' Login no sistema '''
    if request.method == 'GET':
        return render(request, template_name='login.html')
    elif request.method == 'POST':
        try:
            user = Alunos.objects.filter(nome=request.POST.get('nome')).first()
            if user and user.check_password_user(request.POST.get('password')):
                if user.user is None:
                    new = User.objects.create_user(
                        username='Alunos ' + user.nome, 
                        email=user.email, 
                        password=user.password
                        )
                    new.first_name= 'Alunos', 
                    new.last_name=user.nome
                    perm = Permission.objects.get(codename='views_alunos')
                    new.user_permissions.add(perm)
                    new.save()
                    user.user = new
                    user.save()
                login(request=request ,user=user.user)
                return HttpResponse('logado S2')
            else:
                return HttpResponse('erro na senha')

        except ObjectDoesNotExist:
            return HttpResponse('erro de login ou senha')


@require_http_methods(["GET"])
#@login_required(login_url='/estudantes/alunos/login/')
@permission_required(perm='estudante.views_alunos', login_url='/estudantes/alunos/login/')
def logout_alunos(request):
    ''' Logout no sistema '''
    try:
        logout(request)
        return HttpResponse('Logout realizado com sucesso')
    except:
        return HttpResponse('erro no logout')


@require_http_methods(["GET"])
#@login_required(login_url='/estudantes/alunos/login/')
@permission_required(perm='estudante.views_alunos', login_url='/estudantes/alunos/login/')
def test_alunos(request):
    return HttpResponse('Você está logado corretamente como Aluno')


require_http_methods(["GET"])
def get_alunos(request):
    """Retorna todas as alunos."""
    alunos = Alunos.objects.all()

    resp_json = serializers.serialize("json", alunos)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["GET"])
def get_alunos_matricula(request, matricula):
    """Retorna um aluno."""
    alunos = Alunos.objects.filter(pk=matricula)

    resp_json = serializers.serialize("json", alunos)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["POST"])
def post_alunos(request):
    """Adiciona um aluno."""
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
    """Deleta um aluno."""
    post = Alunos.objects.get(pk=matricula)
    post.delete()

    return HttpResponse("Aluno Deletado com sucesso.")



""" views da Matricula"""
require_http_methods(["GET"])
def get_matricula(request):
    """Retorna todas as matriculas."""
    matricula = Matricula.objects.all()

    resp_json = serializers.serialize("json", matricula)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["GET"])
def get_matricula_id(request, id_matricula):
    """Retorna uma matricula."""
    matricula = Matricula.objects.filter(id_matricula=id_matricula)

    resp_json = serializers.serialize("json", matricula)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["POST"])
def post_matricula(request):
    """Adiciona uma matricula."""
    novo = Matricula()
    novo.id_matricula = get_user_model().objects.get(pk=request.POST["id_matricula"])
    novo.data_matricula = request.POST["data_matricula"]
    novo.usuario_responsavel = request.POST["usuario_responsavel"]
    #novo.curso = request.POST["curso"]
    novo.save()
    return HttpResponse("Matricula criada com Sucesso!")

@require_http_methods(["DELETE"])
def delete_matricula(request, id_matricula):
    """Deleta uma matricula."""
    post = Matricula.objects.get(id_matricula=id_matricula)
    post.delete()

    return HttpResponse("Matricula Deletado com sucesso.")



""" views dos Pais"""
@require_http_methods(["GET","POST"])
def login_pais(request):
    ''' Login no sistema '''
    if request.method == 'GET':
        return render(request, template_name='login.html')
    elif request.method == 'POST':
        try:
            user = Pais.objects.filter(nome_mae=request.POST.get('nome')).first()
            if user and user.check_password_user(request.POST.get('password')):
                if user.user is None:
                    new = User.objects.create_user(
                        username='Pais ' + user.nome_mae, 
                        email=user.email, 
                        password=user.password
                        )
                    new.first_name= 'Pais', 
                    new.last_name=user.nome_mae
                    perm = Permission.objects.get(codename='views_pais')
                    new.user_permissions.add(perm)
                    new.save()
                    user.user = new
                    user.save()
                login(request=request ,user=user.user)
                return HttpResponse('logado S2')
            else:
                return HttpResponse('erro na senha')

        except ObjectDoesNotExist:
            return HttpResponse('erro de login ou senha')


@require_http_methods(["GET"])
#@login_required(login_url='/estudantes/pais/login/')
@permission_required(perm='estudante.views_pais', login_url='/estudantes/pais/login/')
def logout_pais(request):
    ''' Logout no sistema '''
    try:
        logout(request)
        return HttpResponse('Logout realizado com sucesso')
    except:
        return HttpResponse('erro no logout')


@require_http_methods(["GET"])
#@login_required(login_url='/estudantes/pais/login/')
@permission_required(perm='estudante.views_pais', login_url='/estudantes/pais/login/')
def test_pais(request):
    return HttpResponse('Você está logado corretamente como Pais')


require_http_methods(["GET"])
def get_pais(request):
    """Retorna todos os pais."""
    pais = Pais.objects.all()

    resp_json = serializers.serialize("json", pais)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["GET"])
def get_pais_id(request, pais_id):
    """Retorna um par de pais."""
    pais = Pais.objects.filter(pais_id=pais_id)

    resp_json = serializers.serialize("json", pais)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["POST"])
def post_pais(request):
    """Adiciona um par de pais."""
    novo = Pais()
    novo.pais_id = get_user_model().objects.get(pk=request.POST["pais_id"])
    novo.nome_pai = request.POST["nome_pai"]
    novo.nome_mae = request.POST["nome_mae"]
    novo.email = request.POST["email"]
    novo.password = novo.set_password(request.POST["password"])
    novo.save()
    return HttpResponse("Pais criados com Sucesso!")

@require_http_methods(["DELETE"])
def delete_pais(request, pais_id):
    """Deleta um par de pais."""
    post = Pais.objects.get(pais_id=pais_id)
    post.delete()

    return HttpResponse("Pais Deletados com sucesso.")



""" views dos Egressos"""
@require_http_methods(["GET","POST"])
def login_egresso(request):
    ''' Login no sistema '''
    if request.method == 'GET':
        return render(request, template_name='login.html')
    elif request.method == 'POST':
        try:
            user = Egresso.objects.filter(nome_egresso=request.POST.get('nome')).first()
            if user and user.check_password_user(request.POST.get('password')):
                if user.user is None:
                    new = User.objects.create_user(
                        username='Egresso ' + user.nome_egresso, 
                        email=user.email, 
                        password=user.password
                        )
                    new.first_name= 'Egresso', 
                    new.last_name=user.nome_egresso
                    perm = Permission.objects.get(codename='views_egresso')
                    new.user_permissions.add(perm)
                    new.save()
                    user.user = new
                    user.save()
                login(request=request ,user=user.user)
                return HttpResponse('logado S2')
            else:
                return HttpResponse('erro na senha')

        except ObjectDoesNotExist:
            return HttpResponse('erro de login ou senha')


@require_http_methods(["GET"])
#@login_required(login_url='/estudantes/egresso/login/')
@permission_required(perm='estudante.views_egresso', login_url='/estudantes/egresso/login/')
def logout_egresso(request):
    ''' Logout no sistema '''
    try:
        logout(request)
        return HttpResponse('Logout realizado com sucesso')
    except:
        return HttpResponse('erro no logout')


@require_http_methods(["GET"])
#@login_required(login_url='/estudantes/egresso/login/')
@permission_required(perm='estudante.views_egresso', login_url='/estudantes/egresso/login/')
def test_egresso(request):
    return HttpResponse('Você está logado corretamente como Egresso')


require_http_methods(["GET"])
def get_egresso(request):
    """Retorna todos os egressos."""
    egresso = Egresso.objects.all()

    resp_json = serializers.serialize("json", egresso)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["GET"])
def get_egresso_id(request, id_matricula_egresso):
    """Retorna um egresso."""
    egresso = Egresso.objects.filter(id_matricula_egresso=id_matricula_egresso)

    resp_json = serializers.serialize("json", egresso)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["POST"])
def post_egresso(request):
    """Adiciona um Egresso."""
    novo = Egresso()
    novo.id_matricula_egresso = get_user_model().objects.get(pk=request.POST["id_matricula_egresso"])
    novo.nome_egresso = request.POST["nome_egresso"]
    novo.email = request.POST["email"]
    novo.password = novo.set_password(request.POST["password"])
    novo.save()
    return HttpResponse("Egresso criado com Sucesso!")

@require_http_methods(["DELETE"])
def delete_egresso(request, id_matricula_egresso):
    """Deleta um Egresso."""
    post = Egresso.objects.get(id_matricula_egresso=id_matricula_egresso)
    post.delete()

    return HttpResponse("Egresso Deletado com sucesso.")


