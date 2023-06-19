import os  # Importa a biblioteca 'os' para acessar o ambiente do sistema operacional
from datetime import timedelta  # Importa a classe 'timedelta' para manipular intervalos de tempo
from celery import Celery  # Importa a biblioteca 'Celery' para trabalhar com tarefas assíncronas
from django.conf import settings  # Importa as configurações do projeto Django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')  # Define a variável de ambiente 'DJANGO_SETTINGS_MODULE' com o valor 'projeto.settings'

# Cria uma instância da aplicação Celery chamada 'app'
app = Celery('projeto', broker=settings.CELERY_BROKER_URL)

# Configura o objeto 'app' para carregar as configurações do Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Permite que o Celery descubra automaticamente as tarefas definidas nas aplicações instaladas no projeto Django
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Atualiza as configurações do Celery
app.conf.update(
    CELERY_TASK_SERIALIZER='json',  # Define o serializador de tarefas como 'json'
    CELERY_RESULT_SERIALIZER='json',  # Define o serializador de resultados como 'json'
    CELERY_ACCEPT_CONTENT=['application/json'],  # Define o tipo de conteúdo aceito como 'application/json'
    CELERY_TIMEZONE=settings.TIME_ZONE,  # Define a timezone do Celery como a mesma do Django
    CELERY_ENABLE_UTC=True,  # Ativa o UTC
    CELERY_RESULT_PERSISTENT=True,  # Habilita o armazenamento persistente dos resultados das tarefas
    CELERY_TRACK_STARTED=True,  # Rastreia o status de início das tarefas
    CELERY_BROKER_CONNECTION_RETRY=True,  # Ativa a tentativa de reconexão com o corretor
    CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP=True,  # Ativa a tentativa de reconexão ao iniciar
    CELERY_TASK_TIME_LIMIT=300,  # Define o limite de tempo máximo para execução de uma tarefa como 300 segundos (5 minutos)
    CELERY_TASK_SOFT_TIME_LIMIT=300,  # Define o limite de tempo suave para a tarefa como 300 segundos (5 minutos)
)

