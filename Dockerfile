FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

CMD sleep 4 && python3 manage.py migrate --settings=main.settings.docker_postgres && python3 manage.py runserver --settings=main.settings.docker_postgres 0.0.0.0:8000
