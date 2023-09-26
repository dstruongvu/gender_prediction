# pull official base image
# FROM python:3.9.5-slim-buster
# FROM tensorflow/tensorflow
FROM python:3.8.12

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && apt-get install lsof -y
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apt-get update && apt-get install -y gcc
RUN apt-get update && apt-get install -y procps
RUN pip install -r requirements.txt

# copy project
COPY . .
