FROM python:3.9-slim-buster

RUN apt-get update && apt-get install gcc libcurl4-openssl-dev libssl-dev -y && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --upgrade pip
RUN mkdir /src
WORKDIR /src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
