PROJECT_NAME = hash_project

# Имя файла docker-compose
COMPOSE_FILE = docker-compose.yml

# Цель по умолчанию
all: up

# Запуск сервисов
up: 
	docker-compose -f $(COMPOSE_FILE) up -d --build

# Остановка сервисов
down:
	docker-compose -f $(COMPOSE_FILE) down

# Перезапуск сервисов
restart: down up

# Просмотр логов
logs:
	docker-compose -f $(COMPOSE_FILE) logs -f

# Выполнение команды в контейнере (например, для миграций)
exec:
	docker-compose -f $(COMPOSE_FILE) exec <имя_сервиса> <команда>

# Проверка статуса сервисов
ps:
	docker-compose -f $(COMPOSE_FILE) ps

# Удаление неиспользуемых образов и томов (очистка)
clean: down
	docker system prune -a --volumes --force

# Помощь
help:
	@echo "Доступные цели:"
	@echo "  up      - Запуск сервисов"
	@echo "  down    - Остановка сервисов"
	@echo "  restart - Перезапуск сервисов"
	@echo "  logs    - Просмотр логов"
	@echo "  exec    - Выполнение команды в контейнере"
	@echo "  ps      - Просмотр статуса сервисов"
	@echo "  clean   - Удаление неиспользуемых образов и томов"
	@echo "  full    - Запуск, остановка и очистка проекта"

.PHONY: all up down restart logs exec ps clean full help
