from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.http import HttpResponse

from chamados.models import Chamado
from core.forms import ChamadoForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'chamados/index.html')

def cadastro_chamados(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)

        if form.is_valid():
            sccd = request.POST.get('sccd')
            titulo = request.POST.get('titulo')
            descricao = request.POST.get('descricao')
            cliente = request.POST.get('cliente')
            severidade = request.POST.get('severidade')
            Chamado(sccd=sccd, titulo=titulo, descricao=descricao, cliente=cliente, severidade=severidade).save()
            messages.info(request, "Chamado cadastrado!")
        else:
            messages.warning(request, "Chamado não cadastrado")


        return redirect('/cadastro_chamados')

    return render(request, 'chamados/cadastro_chamados.html')

def meus_chamados(request):
    num_chamados = Chamado.objects.all().count
    chamados = Chamado.objects.all()

    context = {
        'num_chamados': num_chamados,
        'chamados': chamados,
    }
    return render(request, 'chamados/meus_chamados.html',context=context)

# detalhes chamado
def detalhe_chamado(request, id):
    chamado_id = Chamado.objects.get(id=id)
    context = {
        'chamado_id': chamado_id,
    }

    return render(request, 'chamados/detalhe_chamado.html', context=context)

# editar chamado
def editar_chamado(request, id):

    chamado_id = Chamado.objects.filter(id=id)
    form = ChamadoForm(request.POST)

    if chamado_id:
        if (request.method == 'POST'):
            sccd = request.POST.get('sccd')
            titulo = request.POST.get('titulo')
            descricao = request.POST.get('descricao')
            cliente = request.POST.get('cliente')
            severidade = request.POST.get('severidade')
            Chamado.objects.filter(id=id).update(sccd=sccd, titulo=titulo, descricao=descricao, cliente=cliente, severidade=severidade)


    context = {'chamado_id': chamado_id,}
    return render(request, 'chamados/editar_chamado.html', context=context)


def detalhe_chamado(request, id):
    detalhes = Chamado.objects.get(id=id)
    # excluir = Chamado.objects.get(id=id)
    # print(excluir)
    # excluir.delete()
    return render(request, 'chamados/detalhe_chamado.html', locals())

def excluir_chamado(request, id):
    excluir = Chamado.objects.get(id=id)
    excluir.delete()
    return redirect('meus_chamados')