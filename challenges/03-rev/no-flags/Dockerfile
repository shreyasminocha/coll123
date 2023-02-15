FROM alpine:3

RUN apk add --no-cache build-base socat

RUN adduser --disabled-password --gecos '' hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker
WORKDIR /home/hacker/

COPY ./no-flags.c /home/hacker
COPY ./Makefile /home/hacker
RUN make

CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:"/home/hacker/no-flags"
