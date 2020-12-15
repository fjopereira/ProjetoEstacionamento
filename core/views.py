import csv

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo, 
    Mensalista,
    MovMensalista
)
from .forms import PessoaForm, VeiculoForm, MovRotativoForm, MensalistaForm, MovMensalistaForm

@login_required
# Create your views here.
def home(request):
    context = {'mensagem': 'Ola mundo...'}
    return render(request, 'core/index.html', context)


@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form, 'pessoa_ativo': 'active' }
    return render(request, 'core/lista_pessoas.html', data)


@login_required
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()    
    return redirect('core_lista_pessoas')


@login_required
def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id) 
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


@login_required
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id) 
    if request.method == 'POST':
        pessoa.delete()     
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_pessoa.html', {'pessoa': pessoa})
    

@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form, 'veiculo_ativo': 'active' }
    return render(request, 'core/lista_veiculos.html', data) 


@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()    
    return redirect('core_lista_veiculos')


@login_required
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id) 
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


@login_required
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id) 
    if request.method == 'POST':
        veiculo.delete()     
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_veiculo.html', {'veiculo': veiculo})
    

@login_required
def lista_movrotativos(request):
    lista_movrotativos = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'lista_movrotativos': lista_movrotativos, 'form': form, 'movrotativo_ativo': 'active' }
    return render(request, 'core/lista_movrotativos.html', data)    


@login_required
def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()    
    return redirect('core_lista_movrotativos')


@login_required
def movrotativo_update(request, id):
    data = {}
    movrotativo = MovRotativo.objects.get(id=id) 
    form = MovRotativoForm(request.POST or None, instance=movrotativo)
    data['movrotativo'] = movrotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativo.html', data)


@login_required
def movrotativo_delete(request, id):
    movrotativo = MovRotativo.objects.get(id=id) 
    if request.method == 'POST':
        movrotativo.delete()     
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_movrotativo.html', {'movrotativo': movrotativo})
    

@login_required
def lista_mensalistas(request):
    lista_mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'lista_mensalistas': lista_mensalistas, 'form': form, 'mensalista_ativo': 'active' }
    return render(request, 'core/lista_mensalistas.html', data) 


@login_required    
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()    
    return redirect('core_lista_mensalistas')


@login_required
def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id) 
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)


@login_required
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id) 
    if request.method == 'POST':
        mensalista.delete()     
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_mensalista.html', {'mensalista': mensalista})
    

@login_required
def lista_movmensalistas(request):
    lista_movmensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'lista_movmensalistas': lista_movmensalistas, 'form': form, 'movmensalista_ativo': 'active' }
    return render(request, 'core/lista_movmensalistas.html', data) 


@login_required
def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()    
    return redirect('core_lista_movmensalistas')


@login_required
def movmensalista_update(request, id):
    data = {}
    movmensalista = MovMensalista.objects.get(id=id) 
    form = MovMensalistaForm(request.POST or None, instance=movmensalista)
    data['movmensalista'] = movmensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update_movmensalista.html', data)


@login_required
def movmensalista_delete(request, id):
    movmensalista = MovMensalista.objects.get(id=id) 
    if request.method == 'POST':
        movmensalista.delete()     
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete_movmensalista.html', {'movmensalista': movmensalista})

from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):
        veiculos = Veiculo.objects.all()
        params = {
            'veiculos': veiculos,
            'request': request,
        }
        return Render.render('core/relatorio.html', params, 'relatorio_veiculos')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio_veiculos.csv"'

        veiculos = Veiculo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'placa', 'Proprietario', 'Cor'])

        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario,
                 veiculo.cor
                 ])

        return response






