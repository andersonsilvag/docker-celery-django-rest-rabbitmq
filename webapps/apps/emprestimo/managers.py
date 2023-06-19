from django.db import models
from .choices import ANALISE, APROVADA, NEGADA

# Classe PropostaManager
class PropostaManager(models.Manager):
       
    # Método para excluir propostas em análise
    def exclude_emanalise(self):
        # Retorna uma consulta excluindo propostas com o status "Analise"
        return self.get_queryset().exclude(status=ANALISE)

    # Método para filtrar propostas em análise
    def filter_emanalise(self):
        # Retorna uma consulta filtrando propostas com o status "Analise"
        return self.get_queryset().filter(status=ANALISE)
