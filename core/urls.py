from django.conf.urls import url, include
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    pessoa_novo,
    veiculo_novo,
    movrotativo_novo,
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
    veiculo_update,
    movrotativo_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    movrotativo_delete,
    mensalista_delete,
    movmensalista_delete

)


urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^pessoa-novo/$', pessoa_novo, name='core_pessoa_novo'),
    url(r'^pessoa-update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),
    url(r'^pessoa-delete(?P<id>\d+)/$', pessoa_delete, name='core_pessoa_delete'),

    url(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^veiculo-novo/$', veiculo_novo, name='core_veiculo_novo'),
    url(r'^veiculo-update/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),
    url(r'^veiculo-delete(?P<id>\d+)/$', veiculo_delete, name='core_veiculo_delete'),

    url(r'^movrotativos/$', lista_movrotativos, name='core_lista_movrotativos'),
    url(r'^movrotativo-novo/$', movrotativo_novo, name='core_movmovrotativo_novo'),
    url(r'^movrotativo-update/(?P<id>\d+)/$', movrotativo_update, name='core_movrotativo_update'),
    url(r'^movrotativo-delete(?P<id>\d+)/$', movrotativo_delete, name='core_movrotativo_delete'),
    
    url(r'^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    url(r'^mensalista-novo/$', mensalista_novo, name='core_mensalista_novo'),
    url(r'^mensalista-update/(?P<id>\d+)/$', mensalista_update, name='core_mensalista_update'),
    url(r'^mensalista-delete(?P<id>\d+)/$', mensalista_delete, name='core_mensalista_delete'),

    url(r'^movmensalistas/$', lista_movmensalistas, name='core_lista_movmensalistas'),
    url(r'^movmensalista-novo/$', movmensalista_novo, name='core_movmensalista_novo'),
    url(r'^movmensalista-update/(?P<id>\d+)/$', movmensalista_update, name='core_movmensalista_update'),
    url(r'^movmensalista-delete(?P<id>\d+)/$', movmensalista_delete, name='core_movmensalista_delete'),

]