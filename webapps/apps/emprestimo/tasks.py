from celery import shared_task  # Importa o decorator shared_task do Celery para definir tarefas assíncronas
from celery.utils.log import get_task_logger  # Importa a função get_task_logger do Celery para registrar logs
from .choices import APROVADA, NEGADA  # Importa as constantes de escolha e seus valores
from .query import aprovada_count_query,negada_count_query
from django.apps import apps  # Importa o módulo apps do Django para acessar os modelos da aplicação
from django.db.models import Count, Case, When # Importação das classes e funções necessárias para a consulta
Proposta = apps.get_model('emprestimo', 'Proposta')  # Obtém o modelo Proposta do aplicativo 'emprestimo'

logger = get_task_logger(__name__)  # Obtém um logger para registrar logs para essa tarefa assíncrona

@shared_task
def analisar_propostas_contingencia():
    #Consulta para obter as contagens de propostas aprovadas e negadas
    query = Proposta.objects.all().aggregate(
            negada_count = negada_count_query,
            aprovada_count = aprovada_count_query,
        )
    aprovada_count = query['aprovada_count']
    negada_count = query['negada_count']

    # Filtrando as propostas em análise
    propostas = Proposta.objects.filter_emanalise()

    # Verificando as contagens para cada proposta e atribuindo o status aprovado ou negado
    for proposta in propostas:
        # Se a quantidade de aprovada maior que negada então negar proposta, senão aprovar
        if aprovada_count > negada_count:
            proposta.negada()  # Chama o método negada() no objeto proposta
            negada_count += 1
        else:
            proposta.aprovada()  # Chama o método aprovada() no objeto proposta
            aprovada_count += 1

@shared_task
def recebendo_proposta(nome_completo, cpf, endereco, valor):
    proposta = Proposta()
    proposta.nome_completo = nome_completo
    proposta.cpf = cpf
    proposta.endereco = endereco
    proposta.valor = valor
    proposta.save()