import io
import re
import time
from datetime import datetime
from telethon.sync import TelegramClient, custom, events

import heroku3
from telethon import Button, custom, events
from telethon.utils import get_display_name, pack_bot_file_id

from userbot import (
    BOT_USERNAME,
    BOTLOG_CHATID,
    CHANNEL,
    CMD_HANDLER,
    GROUP,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    SUDO_HANDLER,
    StartTime,
    tgbot,
    bot,
)
from userbot.modules.sql_helper.bot_blacklists import check_is_black_list
from userbot.modules.sql_helper.bot_starters import (
    add_starter_to_db,
    get_all_starters,
    get_starter_details,
)
from userbot.modules.sql_helper.globals import gvarstatus
from userbot.utils import _format, asst_cmd, callback, reply_id

from .ping import get_readable_time

user = bot.get_me()
botusername = BOT_USERNAME
OWNER = user.first_name
OWNER_ID = user.id


heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


async def setit(event, name, value):
    try:
        heroku_var[name] = value
    except BaseException:
        return await event.edit("**Maaf Gagal Menyimpan Karena ERROR**")


def get_back_button(name):
    return [Button.inline("ʙᴀᴄᴋ", data=f"{name}")]


async def check_bot_started_users(user, event):
    if user.id == OWNER_ID:
        return
    check = get_starter_details(user.id)
    if check is None:
        start_date = str(datetime.now().strftime("%B %d, %Y"))
        notification = f"🔮 **#BOT_START**\n**First Name:** {_format.mentionuser(user.first_name , user.id)} \
                \n**User ID: **`{user.id}`\
                \n**Action: **Telah Memulai saya."
    else:
        start_date = check.date
        notification = f"🔮 **#BOT_RESTART**\n**First Name:** {_format.mentionuser(user.first_name , user.id)}\
                \n**ID: **`{user.id}`\
                \n**Action: **Telah Me-Restart saya"
    try:
        add_starter_to_db(user.id, get_display_name(user), start_date, user.username)
    except Exception as e:
        LOGS.error(str(e))
    if BOTLOG_CHATID:
        await event.client.send_message(BOTLOG_CHATID, notification)

@callback(data=re.compile(b"pmclose"))
async def pmclose(event):
    if event.query.user_id == OWNER_ID:
        await event.delete()

@callback(data=re.compile(b"cmdhndlr"))
async def cmdhndlr(event):
    await event.delete()
    pru = event.sender_id
    var = "CMD_HANDLER"
    name = "CMD Handler/ Trigger"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            f"**Kirim Simbol yang anda inginkan sebagai Handler/Pemicu untuk menggunakan bot\nPenangan Anda Saat Ini adalah** [ `{CMD_HANDLER}` ]\n\nGunakan /cancel untuk membatalkan.",
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            await conv.send_message(
                "Membatalkan Proses Settings VAR!",
                buttons=get_back_button("hndlrmenu"),
            )
        elif len(themssg) > 1:
            await conv.send_message(
                "Handler yang anda masukan salah harap gunakan simbol",
                buttons=get_back_button("hndlrmenu"),
            )
        elif themssg.startswith(("/", "#", "@")):
            await conv.send_message(
                "Simbol ini tidak dapat digunakan sebagai handler, Silahkan Gunakan Simbol lain",
                buttons=get_back_button("hndlrmenu"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{name} **Berhasil diganti Menjadi** `{themssg}`",
                buttons=get_back_button("hndlrmenu"),
            )

@callback(data=re.compile(b"apiset"))
async def apiset(event):
    await event.edit(
        "**Silahkan Pilih VAR yang ingin anda Setting**",
        buttons=[
            [
                Button.inline("ᴀʟɪᴠᴇ", data="alivemenu"),
                Button.inline("ɪɴʟɪɴᴇ", data="inlinemenu"),
            ],
            [
                Button.inline("ʜᴀɴᴅʟᴇʀ", data="hndlrmenu"),
                Button.inline("ᴅᴇᴇᴘ ᴀᴘɪ", data="dapi"),
            ],
            [
                Button.inline("ᴏᴄʀ ᴀᴘɪ", data="ocrapi"),
                Button.inline("ʀᴇᴍᴏᴠᴇ.ʙɢ ᴀᴘɪ", data="rmbgapi"),
            ],
            [Button.inline("ʙᴀᴄᴋ", data="settings")],
        ],
    )

@callback(data=re.compile(b"hndlrmenu"))
async def hndlrmenu(event):
    await event.edit(
        "**Silahkan Pilih VAR yang ingin anda Setting**",
        buttons=[
            [
                Button.inline("ᴄᴍᴅ ʜᴀɴᴅʟᴇʀ", data="cmdhndlr"),
                Button.inline("sᴜᴅᴏ ʜᴀɴᴅʟᴇʀ", data="sdhndlr"),
            ],
            [Button.inline("ʙᴀᴄᴋ", data="apiset")],
        ],
    )

@callback(data=re.compile(b"alivemenu"))
async def alivemenu(event):
    await event.edit(
        "**Silahkan Pilih VAR yang ingin anda Setting**",
        buttons=[
            [
                Button.inline("ᴀʟɪᴠᴇ ᴇᴍᴏᴊɪ", data="alvmoji"),
                Button.inline("ᴀʟɪᴠᴇ ʟᴏɢᴏ", data="alvlogo"),
            ],
            [
                Button.inline("ᴀʟɪᴠᴇ ɴᴀᴍᴇ", data="alvname"),
                Button.inline("ᴀʟɪᴠᴇ ᴛᴇᴋs", data="alvteks"),
            ],
            [
                Button.inline("ᴄʜᴀɴɴᴇʟ", data="alvch"),
                Button.inline("ɢʀᴏᴜᴘ", data="alvgc"),
            ],
            [Button.inline("ʙᴀᴄᴋ", data="apiset")],
        ],
    )


@callback(data=re.compile(b"inlinemenu"))
async def inlinemenu(event):
    await event.edit(
        "**Silahkan Pilih VAR yang ingin anda Setting**",
        buttons=[
            [
                Button.inline("ɪɴʟɪɴᴇ ᴇᴍᴏᴊɪ", data="inmoji"),
                Button.inline("ɪɴʟɪɴᴇ ᴘɪᴄ", data="inpics"),
            ],
            [Button.inline("ʙᴀᴄᴋ", data="apiset")],
        ],
    )

@tgbot.on(events.NewMessage(pattern="/start", func=lambda e: e.is_private))
async def bot_start(event):
    chat = await event.get_chat()
    user = await event.client.get_me()
    if check_is_black_list(chat.id):
        return
    reply_to = await reply_id(event)
    mention = f"[{chat.first_name}](tg://user?id={chat.id})"
    my_mention = f"[{user.first_name}](tg://user?id={user.id})"
    first = chat.first_name
    last = chat.last_name
    fullname = f"{first} {last}" if last else first
    username = f"@{chat.username}" if chat.username else mention
    userid = chat.id
    my_first = user.first_name
    my_last = user.last_name
    my_fullname = f"{my_first} {my_last}" if my_last else my_first
    my_username = f"@{user.username}" if user.username else my_mention
    if chat.id != OWNER_ID:
        customstrmsg = gvarstatus("START_TEXT") or None
        if customstrmsg is not None:
            start_msg = customstrmsg.format(
                mention=mention,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
            )
        else:
            start_msg = f"**👋 Hai** {mention}**!**\
                        \n\n**Saya adalah {my_first}** \
                        \n**Anda dapat menghubungi [{OWNER}](tg://user?id={OWNER_ID}) dari sini.**\
                        \n**Jangan melakukan spam atau anda akan di Banned**\
                        \n\n**Powered by** [UserBot](https://github.com/SendiAp/Rose-Userbot)"
        buttons = [
            (
                Button.url("ɢʀᴏᴜᴘ", f"https://t.me/{GROUP}"),
                Button.url("ᴄʜᴀɴɴᴇʟ", f"https://t.me/{CHANNEL}"),
            )
        ]
    else:
        start_msg = f"**Halo [{OWNER}](tg://user?id={OWNER_ID})**\
            \n**Apa ada yang bisa saya bantu?**"
        buttons = [
            (Button.inline("sᴇᴛᴛɪɴɢs ᴠᴀʀ", data="apiset"),),
            (
                Button.inline("ᴘᴍʙᴏᴛ", data="pmbot"),
                Button.inline("ᴜsᴇʀs", data="users"),
            ),
            (
                Button.inline("ᴘɪɴɢ", data="pingbot"),
                Button.inline("ᴜᴘᴛɪᴍᴇ", data="uptimebot"),
            ),
            (Button.inline("ᴄʟᴏsᴇ", data="pmclose"),),
        ]
    try:
        await event.client.send_message(
            chat.id,
            start_msg,
            link_preview=False,
            buttons=buttons,
            reply_to=reply_to,
        )
    except Exception as e:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**ERROR:** Saat Pengguna memulai Bot anda.\n`{e}`",
            )

    else:
        await check_bot_started_users(chat, event)


@tgbot.on(events.NewMessage(pattern="/ping"))
async def _(event):
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await tgbot.send_message(event.chat_id, "🏓**Pong!**\n`%sms`" % duration)
