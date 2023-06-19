from django.contrib import admin
from django.db import models
from .query import analise_count_query,aprovada_count_query,negada_count_query
from django.apps import apps
Proposta = apps.get_model('emprestimo', 'Proposta')

# Registrando o modelo Proposta no admin do Django
@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    # Número de itens exibidos por página
    list_per_page = 100

    # Colunas exibidas na lista de objetos
    list_display = ('id','nome_completo','cpf','status')

    # Colunas da lista que são links para detalhes do objeto
    list_display_links = ('id','nome_completo',)

    # Filtros disponíveis para os objetos
    list_filter = ('status',)

    # Campos pelos quais é possível realizar busca
    search_fields = ['id', 'nome_completo','cpf']

    # Campos que são somente leitura
    readonly_fields = ('status',)
    change_list_template = "consulta/change_list.html"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        response = super().changelist_view(request, extra_context)
        change_list = response.context_data['cl']
        queryset = change_list.queryset

        query = queryset.aggregate(
            analise_count = analise_count_query,
            negada_count = negada_count_query,
            aprovada_count = aprovada_count_query,
        )
        print(query)
        print( query['analise_count'])
        analise = query['analise_count']
        aprovadas = query['aprovada_count']
        negadas = query['negada_count']

        total = analise + aprovadas + negadas

        response.context_data['analise'] = analise
        response.context_data['aprovadas'] = aprovadas
        response.context_data['negadas'] = negadas
        response.context_data['total'] = total
        return response
