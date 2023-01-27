FROM alpine:3

RUN apk add --update --no-cache nodejs npm iputils

RUN adduser --disabled-password --gecos '' hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker
WORKDIR /home/hacker/

COPY ./index.mjs /home/hacker
COPY ./package.json /home/hacker
COPY ./package-lock.json /home/hacker

RUN npm install

CMD node /home/hacker/index.mjs
