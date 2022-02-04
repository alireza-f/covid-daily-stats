FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . /covid-stats
WORKDIR /covid-stats
RUN pip install -r requirements.txt

COPY . /covid-stats/