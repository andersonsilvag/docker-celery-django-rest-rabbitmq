from django.apps import AppConfig  # Importa a classe AppConfig do Django

class ApiConfig(AppConfig):
    name = 'apps.api'  # Define o nome da configuração do aplicativo
    label = 'api'  # Define a etiqueta do aplicativo
    verbose_name = ('Api')  # Define o nome legível do aplicativo

    #def ready(self):
        #import apps.api.signals