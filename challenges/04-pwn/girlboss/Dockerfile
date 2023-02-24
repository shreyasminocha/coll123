FROM archlinux:base-devel

RUN pacman -Sy
RUN pacman -S --noconfirm socat

RUN useradd -m hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker
RUN touch /home/hacker/flag.txt
RUN touch /home/hacker/password.txt
RUN chown root:hacker /home/hacker/flag.txt /home/hacker/password.txt
RUN chmod 440 /home/hacker/flag.txt /home/hacker/password.txt
WORKDIR /home/hacker/

COPY ./password.txt /home/hacker
COPY ./flag.txt /home/hacker
COPY ./girlboss /home/hacker

CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:"/home/hacker/girlboss"
