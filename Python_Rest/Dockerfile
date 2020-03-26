FROM python:3.7-slim

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
	
MKDIR /app

WORKDIR /app

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]