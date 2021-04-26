FROM ubuntu:bionic
WORKDIR /var/app
#COPY main2.py ./
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.8
CMD [ "python3", "./main2.py"]
