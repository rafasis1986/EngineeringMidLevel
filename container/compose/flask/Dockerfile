FROM python:3.5

MAINTAINER Rafael Torres <rdtr.sis@gmail.com>

ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements

RUN pip install -r /requirements/prod.txt \
    && groupadd -r flask \
    && useradd -r -g flask flask

COPY . /app

RUN chown -R flask /app

COPY ./container/compose/flask/gunicorn.sh /gunicorn.sh
COPY ./container/compose/flask/celery.sh /celery.sh
COPY ./container/compose/flask/entrypoint.sh /entrypoint.sh

RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /gunicorn.sh \
    && sed -i 's/\r//' /celery.sh \
    && chmod +x /entrypoint.sh \
    && chown flask /entrypoint.sh \
    && chmod +x /gunicorn.sh \
    && chown flask /gunicorn.sh \
    && chmod +x /celery.sh \
    && chown flask /celery.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
