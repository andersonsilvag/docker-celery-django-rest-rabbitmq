from django.db import models  # Importa o módulo models do Django, necessário para definir modelos de banco de dados
from .choices import STATUS_CHOICES, ANALISE, APROVADA, NEGADA  # Importa as constantes de escolha e seus valores
from .managers import PropostaManager  # Importa o gerenciador personalizado


class Proposta(models.Model):  # Define a classe Proposta, que herda da classe Model do Django

    status = models.CharField(
        ("Status"), max_length=128, default=ANALISE, choices=STATUS_CHOICES
    )  # Campo que armazena o status da proposta, usando as constantes de escolha definidas

    nome_completo = models.CharField('Nome Completo', max_length=255)  # Campo para armazenar o nome completo
    cpf = models.CharField('CPF', max_length=14)  # Campo para armazenar o CPF
    endereco = models.CharField('Endereço', max_length=255)  # Campo para armazenar o endereço
    valor = models.DecimalField(
        'Valor do Empréstimo Pretendido', max_digits=10, decimal_places=2
    )  # Campo para armazenar o valor do empréstimo pretendido

    objects = PropostaManager()  # Define o gerenciador personalizado para a classe Proposta

    class Meta:
        verbose_name = 'Proposta'  # Define o nome amigável singular do modelo
        verbose_name_plural = 'Propostas'  # Define o nome amigável plural do modelo

    def __str__(self):
        return self.nome_completo  # Retorna uma representação legível em string do objeto Proposta

    def analise(self):
        self.status = ANALISE  # Define o status da proposta como "Análise"
        self.save()  # Salva as alterações no banco de dados
    analise.alters_data = True  # Indica que esse método altera os dados no banco de dados

    def aprovada(self):
        self.status = APROVADA  # Define o status da proposta como "Aprovada"
        self.save()  # Salva as alterações no banco de dados
    aprovada.alters_data = True  # Indica que esse método altera os dados no banco de dados

    def negada(self):
        self.status = NEGADA  # Define o status da proposta como "Negada"
        self.save()  # Salva as alterações no banco de dados
    negada.alters_data = True  # Indica que esse método altera os dados no banco de dados

