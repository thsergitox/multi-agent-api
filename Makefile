run:
	fastapi dev app/main.py

install:
	python -m venv venv --clear
	. venv/bin/activate && pip install -r requirements.txt --no-deps --ignore-installed