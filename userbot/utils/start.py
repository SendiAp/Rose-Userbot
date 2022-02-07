from datetime import timedelta

from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot
from userbot import CMD_HANDLER as cmd

from userbot.modules.sql_helper.globals import gvarstatus



async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/ca3a9c55d131882ad9af3.jpg",
                caption="🌹 **Rose UserBot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 5.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @Rose_Userbot ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/fckyoupeople1"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
