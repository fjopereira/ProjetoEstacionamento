from django.conf.urls import url, include
from django.urls import path
from .views import home, contato, servico, plano, sobre


urlpatterns = [
    url(r'^$', home, name='website_home'),
    url(r'^contato$', contato, name='website_contato'),
    path('servicos', servico, name='website_servicos'),
    path('planos', plano, name='website_planos'),
    path('sobre', sobre, name='website_sobre'),
]