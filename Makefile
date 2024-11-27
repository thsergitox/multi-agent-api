.PHONY: install run build up down logs

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

build:
	docker build -t searchai-api .

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f