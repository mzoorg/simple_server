FROM ubuntu:bionic
WORKDIR /var/app
COPY client.py ./
COPY requirements.txt ./
RUN sudo apt update
RUN sudo apt install software-properties-common
RUN sudo add-apt-repository ppa:deadsnakes/ppa
RUN sudo apt update
RUN sudo apt install python3.8
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python3", "./client.py"]
