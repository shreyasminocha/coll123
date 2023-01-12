FROM alpine:3

RUN apk add --no-cache python3 socat

RUN adduser --disabled-password --gecos '' hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker
RUN touch /home/hacker/secret.py
RUN chown root:hacker /home/hacker/secret.py
RUN chmod 440 /home/hacker/secret.py
WORKDIR /home/hacker/

COPY ./nc2.py /home/hacker
COPY ./secret.py /home/hacker

CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:"python3 /home/hacker/nc2.py"
