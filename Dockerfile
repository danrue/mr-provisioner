FROM postgres

RUN apt-get update && apt-get install -y vim python3 python3-pip

COPY . /work
WORKDIR /work
RUN pip3 install -r requirements.txt && pip3 install -r requirements.dev.txt

CMD bash
