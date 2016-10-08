FROM python:3.5

MAINTAINER Rafael Torres <rdtr.sis@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y supervisor

RUN mkdir -p /var/log/supervisor

COPY ./container/compose/flask/supervisord.conf  /etc/supervisor/conf.d/supervisord.conf

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements

RUN pip install -r /requirements/prod.txt \
    && groupadd -r flask \
    && useradd -r -g flask flask

COPY . /app

COPY ./container/compose/flask/start.sh /start.sh
COPY ./container/compose/flask/entrypoint.sh /entrypoint.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
