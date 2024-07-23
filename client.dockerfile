FROM python:3.11.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /client

EXPOSE 1883

COPY client /client
COPY script /script 

RUN apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y libpq5 && \
    apt-get install -y netcat && \
    python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt && \
    chmod -R +x /script    


ENV PATH="/client:/script:/venv/bin:$PATH"

CMD ["commands_client.sh"]