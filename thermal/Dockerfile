FROM python:3.9.0a4-alpine3.10
RUN apk update \\
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN python3 -m pip install psycopg2
