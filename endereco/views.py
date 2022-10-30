from django.shortcuts import HttpResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods

# Create your views here.

from endereco.models import Endereco

@require_http_methods(["GET"])
def get_enderecos(request):
    """Retornando os enderecos."""
    enderecos = Endereco.objects.all()

    resp_json = serializers.serialize("json", enderecos)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["GET"])
def get_endereco_id(request, endereco_id):
    # Retornando apenas um endereco.
    endereco = Endereco.objects.filter(pk=endereco_id)

    endereco_json = serializers.serialize("json", endereco)

    return HttpResponse(endereco_json, content_type="application/json")


@require_http_methods(["POST"])
def post_endereco(request):
    """Adicionando um endereco."""
    novo_endereco = Endereco()
    novo_endereco.rua = request.POST["rua"]
    novo_endereco.numero = request.POST["numero"]
    novo_endereco.complemento = request.POST["complemento"]
    novo_endereco.bairro = request.POST["bairro"]
    novo_endereco.cidade = request.POST["cidade"]
    novo_endereco.cep = request.POST["cep"]

    novo_endereco.save()
    
    return HttpResponse("Endereço cadastrado!")

@require_http_methods(["GET"])
def delete_endereco(request, endereco_id):
    # Removendo um endereco
    endereco = Endereco.objects.get(pk=endereco_id)
    endereco.delete()
    return HttpResponse("Endereço excluído!")
