from django.conf.urls import url
from .views import cadastrar_carro, listar_carro, editar_carro, remover_carro

urlpatterns = [
    url(r'^cadastrar_carro/', cadastrar_carro, name='cadastrar_carro'),
    url(r'^listar_carros/', listar_carro, name='listar_carros'),
    url(r'^editar_carro/(?P<pk>[0-9]+)', editar_carro, name='editar_carro'),
    url(r'^remover_carro/(?P<pk>[0-9]+)', remover_carro, name='remover_carro'),
]
