from django.shortcuts import render
from cadastro.models import Cadastro


# Create your views here.
def index(request):
  if (request.method == 'POST'):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    skype = request.POST.get('skype')
    idade = request.POST.get('idade')
    horario = request.POST.get('horario')
    nickPs = request.POST.get('nickPs')
    cadastro = Cadastro(nome=nome, email=email, skype=skype, idade=idade, horario=horario, nickPs=nickPs)
    cadastro.save()
  return render(request, 'index.html')