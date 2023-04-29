FROM python:3.9.5-slim-buster as base

ENV PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000
