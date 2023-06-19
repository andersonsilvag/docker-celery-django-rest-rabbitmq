import random
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.emprestimo.tasks import analisar_propostas_contingencia
from django.apps import apps
Proposta = apps.get_model('emprestimo', 'Proposta')


class Command(BaseCommand):
    help = 'Analisa propostas em contingência de forma manual, em caso de eventualidades'

    def handle(self, *args, **options):
        self.stdout.write('Inicio da análise')
        analisar_propostas_contingencia()
        self.stdout.write('Conclusão da análise')
