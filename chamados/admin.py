from django.contrib import admin
from .models import Chamado, Modulo, Cliente, Modulo_Cliente, Analise


# Register your models here.
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'dtAbertura', 'dtVencimento', 'dtEncaminhamento', 'severidade',)
admin.site.register(Chamado, ChamadoAdmin)


# TODO: configuraçao para o analista
# class AnalistaAdmin(admin.ModelAdmin):
#     list_display = ('nome',)
# admin.site.register(Analista, AnalistaAdmin)


class ModuloAdmin(admin.ModelAdmin):
    list_display = ('nome',)
admin.site.register(Modulo, ModuloAdmin)


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', )
admin.site.register(Cliente, ClienteAdmin)
