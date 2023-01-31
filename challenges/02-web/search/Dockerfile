FROM alpine:3

RUN apk add --no-cache python3 py3-pip

RUN adduser --disabled-password --gecos '' hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker

COPY src /home/hacker/src
RUN chown root:hacker /home/hacker/src/secret.py
RUN chmod -R 440 /home/hacker/src

WORKDIR /home/hacker/src

RUN python setup.py
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:8000 app:app
