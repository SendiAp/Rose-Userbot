FROM vckyouuu/geezprojects:buster

RUN git clone -b master https://github.com/SendiAp/Rose-Userbot  /home/geezprojects/ \
    && chmod 777 /home/geezprojects \
    && mkdir /home/geezprojects/bin/

WORKDIR /home/geezprojects/

CMD [ "bash", "start" ]
