FROM python:3.6.8

ENV PYTHONBUFFERED=1

WORKDIR /src

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

#CMD ["python3","manage.py","runserver"]

