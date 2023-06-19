from rest_framework import serializers  # Importa a classe serializers do módulo rest_framework
from django.apps import apps  # Importa o módulo apps do Django
Proposta = apps.get_model('emprestimo', 'Proposta')  # Obtém o modelo Proposta do aplicativo 'emprestimo'

class PropostaAdminSerializer(serializers.ModelSerializer):
    obj = serializers.IntegerField()   

    @cached_property
    def all_obj(self):
        # Recupera todos os objetos Proposta do banco de dados e seleciona apenas o campo "id"
        queryset = Proposta.objects.all().values("id")
        # Cria uma lista contendo todos os valores de "id" dos objetos
        obj = [obj['id'] for obj in queryset]
        return obj

    def validate(self, attrs):
        _obj = attrs.get("obj")
        if _obj not in self.all_obj:
            # Lança uma exceção de validação se o valor de "obj" não estiver presente na lista de todos os objetos
            raise serializers.ValidationError(
                f"Invalid obj {_obj} - object does not exist.")
        return super().validate(attrs)

    class Meta:
        model = Proposta  # Define o modelo a ser serializado
        fields = '__all__'  # Define todos os campos do modelo a serem incluídos na serialização

class PropostaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proposta  # Define o modelo a ser serializado
        fields = ['id', 'nome_completo', 'cpf', 'endereco', 'valor']  # Define os campos do modelo a serem incluídos na serialização

