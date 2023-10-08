FROM ubuntu:latest
LABEL authors="anthony"

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

RUN mkdir /home/backend
COPY backend/ /home/backend

RUN mkdir /home/shellhacks_algorithm
COPY shellhacks_algorithm/ /home/shellhacks_algorithm

COPY requirements.txt /home/
COPY start.sh /

RUN apt-get install ffmpeg -y

RUN python3 -m pip install -r /home/requirements.txt
RUN chmod +x start.sh

CMD ./start.sh
