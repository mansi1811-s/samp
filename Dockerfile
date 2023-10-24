#Vulnerable python package 
FROM python:3.5-slim-buster

#FROM python:3.8-slim

WORKDIR /app

COPY main.py /app

RUN apt-get update && apt-get install -y \
    sqlite3

COPY requirements.txt /app
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
