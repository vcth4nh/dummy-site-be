FROM python:3.9.19-alpine3.20

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]