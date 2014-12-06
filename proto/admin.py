from datetime import datetime, timedelta
from django.contrib import admin
from proto.models import Aluno, Atendente, TipoDocumento, Documentos, StatusDocumento, Servico

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nomeUsuario', 'matricula')

class AtendenteAdmin(admin.ModelAdmin):
    list_display = ['nomeUsuario']

class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ['descricao']

class DocumentosAdmin(admin.ModelAdmin):
    list_display = ('tipoDocumento', 'preco', 'tempo', 'descricao')


class StatusDocumentoAdmin(admin.ModelAdmin):
    list_display = ['status']

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('documento', 'aluno', 'status', 'dataSolicitada', 'dataEntrega')
    readonly_fields = ('dataSolicitada', 'dataEntrega')

    def save_model(self, request, obj, form, change):
        obj.aluno = request.user
        obj.save()



admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Atendente, AtendenteAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Documentos, DocumentosAdmin)
admin.site.register(StatusDocumento, StatusDocumentoAdmin)
admin.site.register(Servico, ServicoAdmin)




