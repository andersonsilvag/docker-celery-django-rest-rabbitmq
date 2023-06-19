.PHONY: build up down

IMAGE_NAME = django-docker:latest

# Constrói a imagem Docker
build:
	docker build -t $(IMAGE_NAME) .

# Constrói a imagem e inicia todos os serviços localmente usando o docker-compose
up: build
	docker compose -f docker-compose.yml up

# Para e remove todos os contêineres e imagens
down:
	docker compose down --remove-orphans --rmi 'local'