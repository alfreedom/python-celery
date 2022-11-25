FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH /app
WORKDIR /app

COPY ./requirements.txt /requirements.txt
RUN pip install -U pip && pip install --no-cache-dir -r /requirements.txt

COPY app1/ .
COPY ./docker/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]