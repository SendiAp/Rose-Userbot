from telethon.tl.functions.channels import InviteToChannelRequest

from userbot import BOT_USERNAME
from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import bot, ROSE2, ROSE3, ROSE4, ROSE5, branch

MSG_ON = """
🌹 **Rose-Userbot Berhasil Di Aktifkan**
❍▸ **Userbot Version -** `{}@{}`
❍▸ **Ketik** `{}ping` **untuk Mengecheck Bot**
❍▸ **Created By** {}
"""
try:
    user = bot.get_me()
    mention = f"[{user.first_name}](tg://user?id={user.id})"
except BaseException:
    pass


async def rose_userbot_on():
    try:
        if bot:
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    f"🌹 **Rose-Userbot Berhasil Di Aktifkan**\n\n❍▸ **Userbot Version -** `{version}@{branch}`\n❍▸ **Ketik** `{cmd}ping` **untuk Mengecheck Bot**\n\n",
                )
    except BaseException:
        pass
    try:
        if ROSE2:
            if BOTLOG_CHATID != 0:
                await ROSE2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if ROSE3:
            if BOTLOG_CHATID != 0:
                await ROSE3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if ROSE4:
            if BOTLOG_CHATID != 0:
                await ROSE4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        if ROSE5:
            if BOTLOG_CHATID != 0:
                await ROSE5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
