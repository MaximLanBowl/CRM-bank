FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bankruptcy_crm .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bankruptcy_crm.wsgi"]

