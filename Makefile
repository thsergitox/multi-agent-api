run:
	. venv/bin/activate && uvicorn app.main:app --reload

install:
	python -m venv venv --clear
	. venv/bin/activate && pip install -r requirements.txt --no-deps --ignore-installed