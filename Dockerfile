# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# Lah U cp Atur atur
# Geez-UserBot
#
RUN git clone -b Rose-Userbot https://github.com/skuyykek69/KEK-USERBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/SendiAp/Rose-Userbot/Rose-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
