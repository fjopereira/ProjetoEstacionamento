from django.shortcuts import render
from .models import Contato, Servico, Sobre, Plano

# Create your views here.
def home(request):
    return render(request, 'website/index.html', {'home': 'active'})


def contato(request):
    mensagem = ''
    
    if request.method == 'POST':

        try:

            contato = {}
            contato['email'] = request.POST.get('email')
            contato['nome'] = request.POST.get('nome')
            contato['sobrenome'] = request.POST.get('sobrenome')
            contato['endereco'] = request.POST.get('endereco')
            contato['mensagem_contato'] = request.POST.get('mensagem_contato') 
            contato['receber_noticias'] = True if request.POST.get('receber_noticias') == 'on' else False

            Contato.objects.create(**contato)

        except Exception as e:

            mensagem = str(e)
        else:

            mensagem = 'Contato realizado com sucesso'

    return render(request, 'website/contato.html', {'contatos': 'active', 'mensagem': mensagem })


def servico(request):
    #texto = Servico.objects.filter(id=1).values('servico')
    s = Servico.objects.get(id=1)
    texto1 =  s.texto1
    #print(texto)
    return render(request, 'website/servicos.html', {'servicos': 'active', 'texto1': texto1})


def plano(request):
    p = Plano.objects.get(id=1)
    texto1 = p.texto1
    texto2 = p.texto2
    textos = {'planos': 'active', 'texto1': texto1, 'texto2': texto2}
    return render(request, 'website/planos.html', textos)


def sobre(request):
    s = Sobre.objects.get(id=1)
    texto1 = s.texto1
    texto2 = s.texto2
    textos = {'sobre': 'active', 'texto1': texto1, 'texto2': texto2}
    return render(request, 'website/sobre.html', textos)

