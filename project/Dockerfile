FROM python:3.11-bullseye

WORKDIR /usr/src/project

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /usr/src/project

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000