from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos!")
    return redirect('/')


@login_required(login_url='/login/')
def Lista_eventos(request):
    #lista com filtro por usuario
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)

    #Lista todos os eventos
    #evento = Evento.objects.all()

    dados = {'eventos':evento}
    return render(request,'agenda.html',dados)

