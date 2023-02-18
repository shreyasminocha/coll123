FROM python:3

RUN adduser --disabled-password --gecos '' hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker

COPY src /home/hacker/src
RUN chown root:hacker /home/hacker/src/secret.py
RUN chmod -R 440 /home/hacker/src
RUN chmod 440 /home/hacker/src/secret.py

WORKDIR /home/hacker/src

RUN pip install -r requirements.txt
RUN playwright install chromium
RUN playwright install-deps
# CMD python app.py
CMD gunicorn --bind 0.0.0.0:8000 app:app
