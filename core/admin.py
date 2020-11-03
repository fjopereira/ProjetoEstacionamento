from django.contrib import admin


from .models import(
    Marca, 
    Veiculo, 
    Pessoa, 
    Parametro,
    MovRotativo,
    Mensalista,
    MovMensalista
)


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'checkin', 
        'checkout', 
        'valor_hora', 
        'pagamento', 
        'total', 
        'hora_total',
        'veiculo',
        'teste'
    )

    #para retornar uma informação fixa 
    def teste(self, obj):
        return 'teste'


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = (
        'mensalista',
        'dt_pgto',
        'total'
    )



admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametro)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)
