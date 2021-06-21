FROM python:3.10.0b2-alpine3.13
WORKDIR /var/app
#COPY client.py ./
COPY requirements.txt ./
RUN apt-get update; \
    python3 -m pip install --no-cache-dir -r requirements.txt
#CMD [ "python3", "./client.py"]
