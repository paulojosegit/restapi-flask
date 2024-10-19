FROM python:3.14.0a1-alpine3.20

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY app.py

