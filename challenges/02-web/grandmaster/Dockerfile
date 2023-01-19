FROM archlinux:base-devel

RUN useradd -m hacker
RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm python python-pip git

USER hacker
WORKDIR /home/hacker
RUN git clone https://aur.archlinux.org/stockfish.git
WORKDIR stockfish
RUN makepkg -s
RUN ls -l
USER root
RUN pacman -U --noconfirm stockfish-1:15.1-1-x86_64.pkg.tar.zst
WORKDIR ..

RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker

COPY src /home/hacker/src
RUN chown root:hacker /home/hacker/src/flag.txt
RUN chmod -R 440 /home/hacker/src
RUN chmod 440 /home/hacker/src/flag.txt

WORKDIR /home/hacker/src

RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:8000 app:app
