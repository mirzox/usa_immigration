FROM python:3.11

ARG BUILD_VERSION

LABEL name="vlad_immigration" \
      version=$BUILD_VERSION

RUN mkdir -p /data/django/app
RUN mkdir /data/django/app/logs

WORKDIR /data/django/app

COPY requirements.txt /data/django/app
RUN python3 -m venv venv
RUN . venv/bin/activate && python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . /data/django/app
