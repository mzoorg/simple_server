FROM ubuntu:bionic
WORKDIR /var/app
#COPY client.py ./
COPY requirements.txt ./
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.8 python3-pip tcpdump curl
RUN python3 -m pip install --no-cache-dir -r requirements.txt
#CMD [ "python3", "./client.py"]
