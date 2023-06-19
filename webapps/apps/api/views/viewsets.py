from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from apps.api.serializers import PropostaSerializer, PropostaAdminSerializer
from rest_framework.response import Response
from rest_framework import status
from apps.emprestimo.tasks import recebendo_proposta

from django.apps import apps
Proposta = apps.get_model('emprestimo', 'Proposta')

class Pagination(PageNumberPagination):
    page_size = 10  # Define a quantidade de itens por página
    page_size_query_param = 'page_size'  # Parâmetro para definir o tamanho da página
    max_page_size = 100  # Define o tamanho máximo da página
    default_limit = 10  # Define a quantidade de itens por página (limit)
    max_limit = 100  # Define o limite máximo de itens por página (limit)

class PropostaAdminViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]  # Define as permissões necessárias para acessar as views deste viewset
    pagination_class = Pagination  # Define a classe de paginação a ser usada
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Define os backends de filtragem e ordenação a serem usados
    filterset_fields = ['nome_completo', 'cpf']  # Define os campos pelos quais é possível filtrar
    search_fields = ['nome_completo', 'cpf']  # Define os campos para pesquisa por termo
    ordering_fields = ['status']  # Define os campos pelos quais é possível ordenar
    queryset = Proposta.objects.all()  # Define o conjunto de objetos a serem retornados
    serializer_class = PropostaAdminSerializer  # Define o serializer a ser usado para a serialização dos dados

class PropostaViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Proposta.objects.exclude_emanalise()
    serializer_class = PropostaSerializer

    def get_permissions(self):
        if self.action == 'create':
            return []
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        # Chame a tarefa em segundo plano
        recebendo_proposta.delay(serializer.data['nome_completo'],
                                 serializer.data['cpf'],
                                 serializer.data['endereco'],
                                 serializer.data['valor'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)

