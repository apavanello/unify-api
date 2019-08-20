FROM python:3.7

MAINTAINER apavanello@live.com

ADD . /usr/app

RUN cd /usr/app \
    && pip install pipenv \
    && pipenv lock --requirements > requirements.txt \
    && pip install -r requirements.txt

WORKDIR /usr/app/src
CMD ["flask", "run", "--host=0.0.0.0"]

