FROM python:3.12-slim

RUN mkdir /bot/
WORKDIR bot

ENV PIP_ROOT_USER_ACTION=ignore

COPY . .

RUN pip install -r requirements.txt