FROM python:3.10

RUN apt-get -yyy update && apt-get -yyy install software-properties-common && \
    wget -O- https://apt.corretto.aws/corretto.key | apt-key add - && \
    add-apt-repository 'deb https://apt.corretto.aws stable main'

RUN apt-get -yyy update && apt-get -yyy install java-1.8.0-amazon-corretto-jdk ghostscript

COPY ./requirements/ ./requirements/
RUN pip install -r requirements/dev.txt

ADD . /app
ADD . /anvil-data

RUN useradd anvil
RUN chown -R anvil:anvil /app
RUN chown -R anvil:anvil /anvil-data
RUN chown -R anvil:anvil /usr/local/lib/python3.10
USER anvil

WORKDIR /app
