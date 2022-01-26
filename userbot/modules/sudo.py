import os

import heroku3
from telethon.tl.functions.users import GetFullUserRequest

from userbot import CMD_HANDLER as cmd
from userbot import HEROKU_API_KEY, HEROKU_APP_NAME, SUDO_HANDLER, SUDO_USERS, bot
from userbot.utils import edit_delete, rose_cmd

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USERS") or ""


@bot.on(rose_cmd(outgoing=True, pattern="sudo(?: |$)(.*)"))
async def sudo(event):
    sudo = "True" if SUDO_USERS else "False"
    users = sudousers
    if sudo == "True":
        await event.edit(
            f"🔮 **Sudo:** `Enabled`\n\n📚 ** List Sudo Users:**\n» `{users}`\n\n**SUDO_HANDLER:** `{SUDO_HANDLER}`",
        )
    else:
        await edit_delete(event, "🔮 **Sudo:** `Disabled`")


@bot.on(rose_cmd(outgoing=True, pattern="addsudo(?: |$)(.*)"))
async def add(event):
    suu = event.text[9:]
    if f"{cmd}add " in event.text:
        return
    if event.sender_id in SUDO_USERS:
        return
    event = await event.edit("`Processing...`")
    var = SUDO_USERS
    reply = await event.get_reply_message()
    if not suu and not reply:
        return await edit_delete(
            event,
            "Balas ke pengguna atau berikan user id untuk menambahkannya ke daftar pengguna sudo anda.",
            45,
        )
    if suu and not suu.isnumeric():
        return await edit_delete(
            event, "Berikan User ID atau reply ke pesan penggunanya.", 45
        )
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            event,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan pengguna sudo**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    if suu:
        target = suu
    elif reply:
        target = await get_user(event)
    suudo = f"{sudousers} {target}"
    newsudo = suudo.replace("{", "")
    newsudo = newsudo.replace("}", "")
    await event.edit(
        f"**Berhasil Menambahkan** `{target}` **ke Pengguna Sudo.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
    )
    heroku_Config[var] = newsudo


@bot.on(rose_cmd(outgoing=True, pattern="delsudo(?: |$)(.*)"))
async def _(event):
    if event.sender_id in SUDO_USERS:
        return
    suu = event.text[8:]
    event = await event.edit("`Processing...`")
    reply = await event.get_reply_message()
    if not suu and not reply:
        return await edit_delete(
            event,
            "Balas ke pengguna atau berikan user id untuk menghapusnya dari daftar pengguna sudo Anda.",
            45,
        )
    if suu and not suu.isnumeric():
        return await edit_delete(
            event, "Berikan User ID atau reply ke pesan penggunanya.", 45
        )
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            event,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menghapus pengguna sudo**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    if suu != "" and suu.isnumeric():
        target = suu
    elif reply:
        target = await get_user(event)
    gett = str(target)
    if gett in sudousers:
        newsudo = sudousers.replace(gett, "")
        await event.edit(
            f"**Berhasil Menghapus** `{target}` **dari Pengguna Sudo.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
        )
        var = "SUDO_USERS"
        heroku_Config[var] = newsudo
    else:
        await edit_delete(
            event, "**Pengguna ini tidak ada dalam Daftar Pengguna Sudo anda.**", 45
        )


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    return replied_user.user.id
