
from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot




async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/ca3a9c55d131882ad9af3.jpg",
                caption="š¹ **Rose UserBot Has Been Actived**!!\nāāāāāāāāāāāāāāā\nā  **Userbot Version** - 5.0@master\nāāāāāāāāāāāāāāā\nā  **Powered By:** @Rose_Userbot ",
                buttons=[(Button.url("ź±į“į“į“į“Źį“", "https://t.me/fckyoupeople1"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
