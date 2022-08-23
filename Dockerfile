FROM python:3.10

RUN mkdir -p /backend
WORKDIR /backend

ENV PYTHONUNBUFFERED 1 \
    PYTHONPATH="."

ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --upgrade pip
RUN pip install pipenv

COPY . .

RUN pipenv install --system --deploy

