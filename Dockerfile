FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install alembic psycopg2

COPY ./app /app
COPY alembic.ini /app/alembic.ini
COPY alembic /app/alembic
