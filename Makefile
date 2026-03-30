.PHONY: up down test logs ps

up:
	docker compose up -d --build

down:
	docker compose down

test:
	docker compose ps
	curl -s http://localhost:8090/health
	curl -s http://localhost:8090/stats

logs:
	docker compose logs -f

ps:
	docker compose ps
