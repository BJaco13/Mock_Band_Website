FROM pypy:latest

COPY requirements.txt /opt/app/

WORKDIR /app
COPY . /app
CMD python hello.py