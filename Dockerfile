FROM python:3.7

MAINTAINER apavanello@live.com

RUN mkdir /usr/src/app

RUN cd /usr/src/app \
    && git clone --single-branch --branch docker https://gitlab.com/apavanello/api-unify.git . \
    && pip install pipenv \
    && pipenv lock --requirements > requirements.txt \
    && pip install -r requirements.txt

WORKDIR /usr/src/app/src


