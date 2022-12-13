from django.shortcuts import render

# Create your views here.
"""Views do bar."""

# Create your views here.
from django.shortcuts import HttpResponse
from django.core import serializers

from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.auth.hashers import check_password

from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, permission_required

from gestao.models import Professor, Coordenador, Gestor
from django.core.exceptions import ObjectDoesNotExist


'''
views Professor
'''
@require_http_methods(["GET","POST"])
def login_professor(request):
    ''' Login no sistema '''
    if request.method == 'GET':
        return render(request, template_name='login.html')
    elif request.method == 'POST':
        try:
            user = Professor.objects.filter(nome=request.POST.get('nome')).first()
            if user and user.check_password_user(request.POST.get('password')):
                if user.user is None:
                    new = User.objects.create_user(
                        username='Professor ' + user.nome, 
                        email=user.email, 
                        password=user.password
                        )
                    new.first_name= 'Professor', 
                    new.last_name=user.nome
                    perm = Permission.objects.get(codename='views_professor')
                    new.user_permissions.add(perm)
                    new.save()
                    user.user = new
                    user.save()
                login(request=request, user=user.user)
                return HttpResponse('logado S2')
            else:
                return HttpResponse('erro na senha')

        except ObjectDoesNotExist:
            return HttpResponse('erro de login ou senha')


@require_http_methods(["GET"])
#@login_required(login_url='/gestao/professor/login/')
@permission_required(perm='gestao.views_professor', login_url='/gestao/professor/login/')
def logout_professor(request):
    ''' Logout no sistema '''
    try:
        logout(request)
        return HttpResponse('Logout realizado com sucesso')
    except:
        return HttpResponse('erro no logout')


@require_http_methods(["GET"])
#@login_required(login_url='/gestao/professor/login/')
@permission_required(perm='gestao.views_professor', login_url='/gestao/professor/login/')
def test_professor(request):
    return HttpResponse('Você está logado corretamente como Professor')


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
#@permission_required(perm='gestao.views_professor', login_url='/gestao/professor/login/')
def delete_professor(request, professor_id):
    """Deleta um professor"""
    professor = Professor.objects.get(pk=professor_id)
    professor.delete()

    return HttpResponse("Deletado com sucesso.")


'''
views Coordenador
'''
@require_http_methods(["GET","POST"])
def login_coordenador(request):
    ''' Login no sistema '''
    if request.method == 'GET':
        return render(request, template_name='login.html')
    elif request.method == 'POST':
        try:
            user = Coordenador.objects.filter(nome=request.POST.get('nome')).first()
            if user.check_password_user(request.POST.get('password')):
                if user.user is None:
                    new = User.objects.create_user(
                        username='Coordenador ' + user.nome, 
                        email=user.email, 
                        password=user.password
                        )
                    new.first_name= 'Coordenador', 
                    new.last_name=user.nome
                    perm = Permission.objects.get(codename='views_coordenador')
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
#@login_required(login_url='/gestao/coordenador/login/')
@permission_required(perm='gestao.views_coordenador', login_url='/gestao/coordenador/login/')
def logout_coordenador(request):
    ''' Logout no sistema '''
    try:
        logout(request)
        return HttpResponse('Logout realizado com sucesso')
    except:
        return HttpResponse('erro no logout')


@require_http_methods(["GET"])
#@login_required(login_url='/gestao/coordenador/login/')
@permission_required(perm='gestao.views_coordenador', login_url='/gestao/coordenador/login/')
def test_coordenador(request):
    return HttpResponse('Você está logado corretamente como Coordenador')


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
#@permission_required(perm='gestao.views_coordenador', login_url='/gestao/coordenador/login/')
def delete_coordenador(request, coordenador_id):
    coordenador = Coordenador.objects.get(pk=coordenador_id)
    coordenador.delete()

    return HttpResponse("Deletado com sucesso.")

'''
views Gestor
'''
@require_http_methods(["GET","POST"])
def login_gestor(request):
    ''' Login no sistema '''
    if request.method == 'GET':
        return render(request, template_name='login.html')
    elif request.method == 'POST':
        try:
            user = Gestor.objects.filter(nome=request.POST.get('nome')).first()
            if user and user.check_password_user(request.POST.get('password')):
                if user.user is None:
                    new = User.objects.create_user(
                        username='Gestor ' + user.nome, 
                        email=user.email, 
                        password=user.password
                        )
                    new.first_name= 'Gestor', 
                    new.last_name=user.nome
                    perm = Permission.objects.get(codename='views_gestor')
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
#@login_required(login_url='/gestao/gestor/login/')
@permission_required(perm='gestao.views_gestor', login_url='/gestao/gestor/login/')
def logout_gestor(request):
    ''' Logout no sistema '''
    try:
        logout(request)
        return HttpResponse('Logout realizado com sucesso')
    except:
        return HttpResponse('erro no logout')


@require_http_methods(["GET"])
#@login_required(login_url='/gestao/gestor/login/')
@permission_required(perm='gestao.views_gestor', login_url='/gestao/gestor/login/')
def test_gestor(request):
    return HttpResponse('Você está logado corretamente como Gestor')


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
#@permission_required(perm='gestao.views_gestor', login_url='/gestao/gestor/login/')
def delete_gestor(request, gestor_id):
    gestor = Gestor.objects.get(pk=gestor_id)
    gestor.delete()

    return HttpResponse("Deletado com sucesso.")