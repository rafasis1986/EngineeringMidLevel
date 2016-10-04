FROM node:4.6.0-slim

MAINTAINER Rafael Torres <rdtr.sis@gmail.com>

RUN npm install -g tslint typescript typings gulp

COPY ./knockoutapp /webapp

WORKDIR /webapp

COPY ./container/compose/npm/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]