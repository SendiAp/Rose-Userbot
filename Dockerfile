FROM ghcr.io/sendiap/dockerfile:rose

RUN git clone -b master https://github.com/SendiAp/Rose-Userbot  /home/dockerfile:rose/ \
    && chmod 777 /home/dockerfile:rose \
    && mkdir /home/dockerfile:rose/bin/

WORKDIR /home/dockerfile:rose/

CMD [ "bash", "start" ]
