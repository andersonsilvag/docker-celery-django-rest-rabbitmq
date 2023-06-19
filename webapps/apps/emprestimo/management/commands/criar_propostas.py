import random
from django.core.management.base import BaseCommand
from django.conf import settings

from django.apps import apps
Proposta = apps.get_model('emprestimo', 'Proposta')


class Command(BaseCommand):
    help = 'Cria registros aleatórios de Proposta em ambiente de teste'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='O número total de registros a serem criados')

    def handle(self, *args, **options):
        if settings.DEBUG:
            total = options['total']
            for _ in range(total):
                nome_completo = "Nome Completo Teste"
                cpf = gerar_cpf_aleatorio()
                endereco = "Endereço Aleatório" 
                valor = random.uniform(1000, 10000)
                proposta = Proposta(nome_completo=nome_completo, cpf=cpf, endereco=endereco, valor=valor)
                proposta.save()
            self.stdout.write(self.style.SUCCESS(f'{total} registros de Proposta foram criados com sucesso.'))
        else:
            self.stdout.write('VOCÊ ESTÁ EM AMBIENTE DE PRODUÇÃO, IMPOSSIVEL CRIAR PROPOSTA DE TESTE')


def gerar_cpf_aleatorio():
    cpf = ''
    
    # Gera os 9 primeiros dígitos do CPF
    for _ in range(9):
        cpf += str(random.randint(0, 9))
    
    # Calcula o primeiro dígito verificador
    soma = 0
    for i, digit in enumerate(cpf):
        soma += int(digit) * (10 - i)
    primeiro_digito = (11 - (soma % 11)) % 10
    cpf += str(primeiro_digito)
    
    # Calcula o segundo dígito verificador
    soma = 0
    for i, digit in enumerate(cpf):
        soma += int(digit) * (11 - i)
    segundo_digito = (11 - (soma % 11)) % 10
    cpf += str(segundo_digito)
    
    return cpf        