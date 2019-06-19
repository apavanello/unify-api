FROM python:3.7

MAINTAINER apavanello@live.com

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
RUN git clone https://gitlab.com/apavanello/api-unify.git .

RUN pip install pipenv

RUN pipenv install --system --deploy
