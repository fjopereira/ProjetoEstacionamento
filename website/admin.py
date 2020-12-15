from django.contrib import admin
from .models import Contato, Servico, Sobre, Plano


admin.site.register(Contato)
admin.site.register(Servico)
admin.site.register(Sobre)
admin.site.register(Plano)

# Register your models here.
