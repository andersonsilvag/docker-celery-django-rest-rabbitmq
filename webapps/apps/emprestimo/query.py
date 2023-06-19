from django.db.models import Count, Case, When # Importação das classes e funções necessárias para a consulta
from .choices import ANALISE, APROVADA, NEGADA
aprovada_count_query = Count(
    Case(
        When(status=APROVADA, then=1)
    )
)
negada_count_query= Count(
    Case(
        When(status=NEGADA,then=1)
    )
)

analise_count_query = Count(
    Case(
        When(status=ANALISE,then=1)
    )
)