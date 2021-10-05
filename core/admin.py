from django.contrib import admin
from core.models import Evento



class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','data_evento','data_criacao')      # altera o header da table no admin
    list_filter = ('usuario','data_evento',)                    # cria filtros no admin

admin.site.register(Evento, EventoAdmin)