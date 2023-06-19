from django.apps import AppConfig

# Configuração do aplicativo Emprestimo
class EmprestimoConfig(AppConfig):
    # Define o tipo de campo automático padrão para as tabelas do banco de dados
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nome do aplicativo
    name = 'apps.emprestimo'
    
    # Rótulo do aplicativo
    label = 'emprestimo'
    
    # Nome legível para exibição do aplicativo
    verbose_name = ('emprestimo')

    # Comentado, mas poderia conter ações a serem executadas quando o aplicativo estiver pronto
    #def ready(self):
        #import apps.emprestimo.signals
