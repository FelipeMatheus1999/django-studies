FROM python:3.8

COPY ./requirements /requirements
RUN pip install -r requirements/prod.txt
RUN pip install -r requirements/dev.txt

RUN apt-get update && apt-get upgrade -y && \
python -m pip install psycopg2-binary

WORKDIR /app
COPY . /app/
