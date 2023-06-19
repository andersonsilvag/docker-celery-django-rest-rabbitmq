from rest_framework import serializers  # Importa a classe serializers do módulo rest_framework
from django.apps import apps  # Importa o módulo apps do Django
Proposta = apps.get_model('emprestimo', 'Proposta')  # Obtém o modelo Proposta do aplicativo 'emprestimo'

class PropostaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta  # Define o modelo a ser serializado
        fields = '__all__'  # Define todos os campos do modelo a serem incluídos na serialização

class PropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta  # Define o modelo a ser serializado
        fields = ['id', 'nome_completo', 'cpf', 'endereco', 'valor']  # Define os campos do modelo a serem incluídos na serialização

