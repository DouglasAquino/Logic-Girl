from django.shortcuts import redirect, render
from .models import Cargo, Publicacao, Usuario

def home(request):
    logado = None
    if request.user.is_authenticated:
        logado = request.user
    posts = Publicacao.objects.all()[:3]
    return render(request, "home.html", {"logado":logado,"posts":posts})

def download(request):
    logado = None
    if request.user.is_authenticated:
        logado = request.user
    
    return render(request, "download.html", {"logado":logado})

def avaliacao(request):
    logado = None
    if request.user.is_authenticated:
        logado = request.user
    
    return render(request, "avaliacao.html", {"logado":logado})

def equipe(request):
    logado = None
    if request.user.is_authenticated:
        logado = request.user
    devs = []
    autores = []
    for user in Usuario.objects.all():
        for i in user.cargos.all():
            if "Criador" == i.tipo:
                devs.append(user)
            if "Autor" == i.tipo or "Autora" == i.tipo:
                autores.append(user)
    
    return render(request, "equipe.html", {"logado":logado,"devs":devs,"autores":autores})

def publicacao(request,id):
    if Publicacao.objects.filter(pk=id):
        pub = Publicacao.objects.get(pk=id)
        return render(request, 'publicacao.html',{"publicacao":pub})
    else:
        return redirect("home")
    
def publicacoes(request):
    return render(request, 'publicacoes.html',{"publicacoes":Publicacao.objects.all()})