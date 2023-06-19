from django.conf import settings  # Importa as configurações do Django
from django.urls import path, include  # Importa a função path e o módulo include do Django
from rest_framework import routers  # Importa a classe routers do módulo rest_framework
from apps.api.views.viewsets import PropostaViewSet, PropostaAdminViewSet  # Importa os viewsets PropostaViewSet e PropostaAdminViewSet do módulo apps.api.views.viewsets

app_name = 'api'  # Define o nome do aplicativo

router = routers.DefaultRouter()  # Cria um objeto router da classe DefaultRouter
router.register(r'propostaAdmin', PropostaAdminViewSet)  # Registra o viewset PropostaAdminViewSet na rota 'propostaAdmin'
router.register(r'proposta', PropostaViewSet)  # Registra o viewset PropostaViewSet na rota 'proposta'

urlpatterns = [
    path('', include(router.urls)),  # Inclui as URLs definidas pelo router nas urlpatterns
]
