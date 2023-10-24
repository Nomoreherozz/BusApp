# FROM python:3.9.1-alpine3.13
# LABEL maintainer="londonappdeveloper.com"

# ENV PYTHONUNBUFFERED 1

# COPY ./requirements.txt /requirements.txt
# COPY ./app /app

# RUN mkdir /app
# WORKDIR /app
# EXPOSE 8000

# RUN python -m venv /py && \
#     /py/bin/pip install --upgrade pip && \
#     apk add --update --no-cache postgresql-client && \
#     apk add --update --no-cache --virtual .tmp-deps \
#         build-base postgresql-dev musl-dev && \
#     /py/bin/pip install -r /requirements.txt && \
#     apk del .tmp-deps && \
#     adduser --disabled-password --no-create-home app

# ENV PATH="/py/bin:$PATH"

# USER app


FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# Install postgres client
# RUN apk add --update --no-cache postgresql-client

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# [Security] Limit the scope of user who run the docker image
RUN adduser -D user

USER user
