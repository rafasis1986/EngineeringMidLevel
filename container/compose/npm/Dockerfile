FROM node:4.6.0-slim

MAINTAINER Rafael Torres <rdtr.sis@gmail.com>

RUN npm install -g tslint typescript typings gulp

# COPY ./knockoutapp /webapp
RUN mkdir /webapp

COPY ./container/compose/npm/entrypoint.sh /entrypoint.sh

RUN groupadd -r webapps && useradd -r -g webapps flask

RUN chown -R flask /webapp

RUN chmod +x /entrypoint.sh && chown flask /entrypoint.sh

WORKDIR /webapp

ENTRYPOINT ["/entrypoint.sh"]
