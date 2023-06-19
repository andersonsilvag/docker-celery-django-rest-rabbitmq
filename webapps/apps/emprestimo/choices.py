# Definindo as constantes de status
ANALISE, APROVADA, NEGADA = (
    "Analise", "Aprovada", "Negada",)

# Definindo as opções de status como uma tupla de tuplas
STATUS_CHOICES = (
    # Opção de status "Em análise" com o valor ANALISE
    (ANALISE, ("Em análise")),
    # Opção de status "Aprovada" com o valor APROVADA
    (APROVADA, ("Aprovada")),
    # Opção de status "Negada" com o valor NEGADA
    (NEGADA, ("Negada")),
)
