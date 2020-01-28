FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD Docker/python/requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/