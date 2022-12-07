#pull official base image
FROM python:3.8.10

#set wrok directory
WORKDIR /usr/src/app

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNBURRERED 1

# RUN apk update
# RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

COPY . /usr/src/app/

#install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt