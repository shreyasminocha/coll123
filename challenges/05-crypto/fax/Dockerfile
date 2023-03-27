FROM alpine:3

RUN apk add --no-cache python3 py3-pip socat

RUN adduser --disabled-password --gecos '' hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker
WORKDIR /home/hacker/

COPY ./fax.py /home/hacker
COPY ./secret.py /home/hacker
COPY ./requirements.txt /home/hacker

RUN chown root:hacker /home/hacker/secret.py
RUN chmod 440 /home/hacker/secret.py

RUN pip install -r requirements.txt

USER hacker
CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:"python3 /home/hacker/fax.py"
