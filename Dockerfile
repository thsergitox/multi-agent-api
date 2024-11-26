FROM python:3.12-slim

WORKDIR /src

COPY . requirements.txt 

RUN pip install -r requirements.txt

COPY app/ src/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]