FROM archlinux:base-devel

RUN pacman -Sy
RUN pacman -S --noconfirm socat

RUN useradd -m hacker
RUN useradd -m chad
RUN chown -R root:chad /home/hacker/
RUN chmod 755 /home/hacker

WORKDIR /home/hacker/

COPY ./flag.txt /home/hacker
COPY ./sendfile.c /home/hacker
COPY ./seccomp-bpf.h /home/hacker
COPY ./Makefile /home/hacker
RUN make

RUN chown chad:chad /home/hacker/sendfile
RUN chmod 4751 /home/hacker/sendfile

RUN chown chad:chad /home/hacker/flag.txt
RUN chmod 440 /home/hacker/flag.txt

USER hacker
CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:"/home/hacker/sendfile"
