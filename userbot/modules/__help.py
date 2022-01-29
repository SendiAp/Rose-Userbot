# Fixes by SendiAp https://github.com/SendiAp/Rose-Userbot
# t.me/pikyus1


import logging

from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from userbot import BOT_USERNAME, bot
from userbot import CMD_HANDLER as cmd
from userbot.utils import edit_or_reply
from userbot.events import rose_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@bot.on(rose_cmd(outgoing=True, pattern=r"helpme"))
async def yardim(event):
    try:
        tgbotusername = BOT_USERNAME
        if tgbotusername is not None:
            results = await event.client.inline_query(tgbotusername, "@RoseUserbot")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`Botnya tidak berfungsi! Silahkan atur Bot Token dan Username dengan benar. Modul telah dihentikan.`"
            )
    except Exception:
        return await event.edit(
            "`Anda tidak dapat mengirim hasil sebaris dalam obrolan ini (disebabkan oleh SendInlineBotResultRequest)`"
        )
