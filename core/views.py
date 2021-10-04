from django.shortcuts import render

from core.models import Evento


def Lista_eventos(request):
    #lista com filtro por usuario
    #usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request,'agenda.html',dados)

