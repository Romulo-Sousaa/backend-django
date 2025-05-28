from django.urls import path
from . import views

urlpatterns = [
    # Produtos
    path('', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.cria_produto, name='cria_produto'),
    path('edita/<int:pk>/', views.edita_produto, name='edita_produto'),
    path('remove/<int:pk>/', views.remove_produto, name='remove_produto'),
    path('detalhe/<int:pk>/', views.detalhe_produto, name='detalhe_produto'),

    # Clientes
    # path('', views.lista_produtos, name='lista_produtos'),
    path('novo_cliente/', views.cria_cliente, name='cria_cliente'),
    path('edita_cliente/<int:pk>/', views.edita_cliente, name='edita_cliente'),
    path('remove_cliente/<int:pk>/', views.remove_cliente, name='remove_cliente'),

    # Vendas
    # path('', views.lista_produtos, name='lista_produtos'),
    path('novo_venda/', views.cria_venda, name='cria_venda'),
    path('edita_venda/<int:pk>/', views.edita_venda, name='edita_venda'),
    path('remove_venda/<int:pk>/', views.remove_venda, name='remove_venda'),

    path('vendas/', views.venda_list, name='venda_list'),
]