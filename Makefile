.PHONY: help install run
.DEFAULT_GOAL := help

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Create venv and install dependencies
	python -m venv venv --clear
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

run: ## Run the FastAPI server with hot reload
	. venv/bin/activate && uvicorn app.main:app --reload