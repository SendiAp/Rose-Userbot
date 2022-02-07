
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
                caption="🌹 **Rose UserBot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 5.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @Rose_Userbot ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/fckyoupeople1"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
       from userbot.modules.sql_helper.globals import delgvar, gvarstatus

        msg_details = gvarstatus("restartstatus").split("\n")
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await tgbot.check_testcases()
            message = await tgbot.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**Ok Bot is Back and Alive.**"
            await tgbot.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartstatus") is not None:
                await drgub.send_message(
                    msg_details[0],
                    f"{cmd}ping",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None
