run:
	fastapi dev app/main.py

install:
	rm -rf venv
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt