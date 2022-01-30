import asyncio
import importlib
import logging
import sys
from pathlib import Path
from random import randint

import heroku3
from telethon.tl.functions.contacts import UnblockRequest

from userbot import (
    BOT_TOKEN,
    BOTLOG_CHATID,
    CMD_HELP,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    LOGS,
    bot,
)

heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


async def autobot():
    if BOT_TOKEN:
        return
    await bot.start()
    await bot.send_message(
        BOTLOG_CHATID, "➕ **Sedang Membuat Bot**...\n\n» Harap Tunggu Beberapa Detik!"
    )
    who = await bot.get_me()
    name = who.first_name + "'s Assistant Bot"
    if who.username:
        username = who.username + "_ubot"
    else:
        username = "rosebot" + (str(who.id))[5:] + "ubot"
    bf = "@BotFather"
    await bot(UnblockRequest(bf))
    await bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if isdone.startswith("Itu tidak bisa saya lakukan."):
        LOGS.info(
            "✖️ **Bot Gagal Dibuat**..\n\n» Silakan buat Bot dari @BotFather dan tambahkan tokennya di var BOT_TOKEN."
        )
        sys.exit(1)
    await bot.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await bot.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await bot.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "✖️ **Bot Gagal Dibuat**..\n\n» Silakan buat Bot dari @BotFather dan tambahkan tokennya di var BOT_TOKEN"
            )
            sys.exit(1)
    await bot.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    await bot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "rosebot" + (str(who.id))[6:] + str(ran) + "ubot"
        await bot.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await bot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            await bot.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(bf, "Search")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_file(bf, "resources/extras/images.jpeg")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setabouttext")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"✨ Hello ✨!! I'm Assistant Bot of {who.first_name}")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(
                bf, f"✨Powerful Rose Assistant Bot✨\n\n✨ Owner ~ {who.first_name} ✨\n\n✨ Powered By ~ @Rose_Userbot ✨"
            )
            await bot.send_message(
                BOTLOG_CHATID,
                f"✔️ **Berhasil Membuat Bot**\n\n» Username Bot Kamu Adalah @{username} .",
            )
            await bot.send_message(
                BOTLOG_CHATID,
                "💣 **Tunggu Sebentar**...\n\n» Sedang Restart Heroku Untuk Menerapkan Perubahan.",
            )
            heroku_var["BOT_TOKEN"] = token
            heroku_var["BOT_USERNAME"] = f"@{username}"
        else:
            LOGS.info(
                "🚧 **Ada Kesahalan Beberapa**...\n\n» Hapus Beberapa Bot Telegram Anda di @Botfather Atau Set Var BOT_TOKEN dengan token bot."
            )
            sys.exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        await bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(bf, "Search")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setuserpic")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_file(bf, "resources/extras/images.jpeg")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setabouttext")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"✨ Hello ✨!! I'm Assistant Bot of {who.first_name}")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setdescription")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(
            bf, f"✨Powerful Rose Assistant Bot✨\n\n✨ Owner ~ {who.first_name} ✨\n\n✨ Powered By ~ @Rose_Userbot ✨"
        )
        await bot.send_message(
            BOTLOG_CHATID,
            f"✔️ **Berhasil Membuat Bot**\n\n» Username Bot Kamu Adalah @{username} .",
        )
        await bot.send_message(
            BOTLOG_CHATID,
            "💣 **Tunggu Sebentar**...\n\n» Sedang Restart Heroku Untuk Menerapkan Perubahan.",
        )
        heroku_var["BOT_TOKEN"] = token
        heroku_var["BOT_USERNAME"] = f"@{username}"
    else:
        LOGS.info(
            "🚧 **Ada Kesahalan Beberapa**...\n\n» Hapus Beberapa Bot Telegram Anda di @Botfather Atau Set Var BOT_TOKEN dengan token bot."
        )
        sys.exit(1)
