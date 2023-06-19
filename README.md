# Docker + Celery + Django + Rest + Rabbitmq = 🔥

Este projeto Django tem como finalidade concluir um desafio técnico para criar um sistema de gestão de propostas de empréstimo pessoal. Os usuários poderão cadastrar propostas de empréstimo pessoal e a avaliação será executada através de uma fila RabbitMQ utilizando o Django Celery. O Django Celery é responsável por avaliar cada proposta e atribuir um status de "Negada" ou "Aprovada". O algoritmo de avaliação de propostas garantirá que metade delas seja negada e a outra metade seja aprovada. Em seguida, o algoritmo atualizará o status da proposta no banco de dados.

## Tecnologias utilizadas
As tecnologias utilizadas neste projeto:
- [`Python`](https://www.python.org) ver. 3.11
- [`Django`](https://www.djangoproject.com) ver. 4.2
- [`PostgreSQL`](https://www.postgresql.org) ver. 15
- [`Docker`](https://docs.docker.com/get-docker/) e [`Docker Compose`](https://docs.docker.com/compose/)
- [`Celery`](https://docs.celeryq.dev/en/stable/) 
- [`Django Rest Framework`](https://www.django-rest-framework.org/) 
- [`RabbitMQ`](https://www.rabbitmq.com/) 
- [`Redis`](https://redis.io/) 


## Recursos
- Configurações individuais podem ser alteradas usando variáveis de ambiente
- Construção e depuração do projeto pode ser realizado em Docker
- O docker-compose cria tudo o que precisa
- Automação da migração do banco de dados e coleta automática de arquivos estáticos ao iniciar ou reiniciar o contêiner Django.
- Automação da criação do primeiro usuário no Django com um login e senha default
- Poucas Dependências

## Configurações do Django
Algumas configurações do Django do arquivo settings.py são armazenadas em variáveis ​​de ambiente. Você pode alterar essas configurações no arquivo .env.

O nome de usuário e senha de super usuário, estão definidos no .env, como o nome e valores iniciais a seguir: DJANGO_SUPERUSER_USERNAME=admin, DJANGO_SUPERUSER_PASSWORD=admin


## Como usar
### Recomenda-se usar linux
### Lembre-se há necessidade de ter instalado previamente o git, docker e docker compose (versão 2.18.1)
No console do linux execute:

    sudo apt-get update && apt-get install ca-certificates curl gnupg - y
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg

    echo \
    "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    sudo apt-get update && apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin make git -y
    
A análise de propostas automática é realizada pelo Celery, utilizando o Celery Beat para agendamento. A configuração de agendamento está definida no arquivo settings.py, no parâmetro "CELERY_BEAT_SCHEDULE", para que a análise seja executada a cada minuto. Fique a vontade para alterar esse tempo.

### O arquivo Makefile contém comandos que podem ser utilizados para executar determinadas ações no docker:

    Use make no console, veja as opções disponiveis:

    `make build`

    Constrói a imagem Docker

    `make up`

    Constrói a imagem e inicia todos os serviços localmente usando o docker-compose
    Agora você pode acessar http://127.0.0.1:9001/ em seu navegador, para cadastrar propostas. Caso queria acompanhar as propostas, vá para o painel de administração do Django acessando http://127.0.0.1:9001/admin/. O superusuário com login e senha admin/admin já está criado.

    `make down`

    Para e remove todos os contêineres e imagens


### O projeto também possui comandos personalizados de gerenciamento do Django, permitindo a criação de propostas aleatórias ou a análise manual de propostas em situações de contingência, saiba mais em (https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/):

Para cadastrar propostas aleatórias, execute o comando "criar_propostas" no gerenciador de tarefas e especifique a quantidade desejada da seguinte maneira, lembre-se de que você precisa estar na pasta webapps:
    
    python manage.py criar_propostas 100

Para avaliar propostas manualmente:
    
    python manage.py analisar_proposta
