# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# Lah U cp Atur atur
# Geez-UserBot
# Kalau Ngedit Yang Bener Ngentot
#
RUN git clone -b Rose-UserBot https://github.com/SendiAp/Rose-UserBot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/SendiAp/Rose-UserBot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
