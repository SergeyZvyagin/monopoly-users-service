FROM python:3.9-slim

WORKDIR /app

COPY ./ ./

RUN pip install -r requirements.txt
CMD python bin/monopoly-lobbies-service.py -c configuration/monopoly-lobbies-service-conf.toml
