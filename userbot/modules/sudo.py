import os

import heroku3

from userbot import CMD_HANDLER as cmd
from userbot import HEROKU_API_KEY, HEROKU_APP_NAME, SUDO_USERS
from userbot.utils import edit_delete, edit_or_reply, rose_cmd

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USERS") or ""


@rose_cmd(pattern="addsudo(?:\\s|$)([\\s\\S]*)")
async def add(event):
    suu = event.text[9:]
    if f"{cmd}add " in event.text:
        return
    if event.sender_id in SUDO_USERS:
        return
    xxnx = await edit_or_reply(event, "`Processing...`")
    var = "SUDO_USERS"
    reply = await event.get_reply_message()
    if not suu and not reply:
        return await edit_delete(
            xxnx,
            "Balas ke pengguna atau berikan user id untuk menambahkannya ke daftar pengguna sudo anda.",
            45,
        )
    if suu and not suu.isnumeric():
        return await edit_delete(
            xxnx, "Berikan User ID atau reply ke pesan penggunanya.", 45
        )
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxnx,
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
    await xxnx.edit(
        f"**Berhasil Menambahkan** `{target}` **ke Pengguna Sudo.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
    )
    heroku_Config[var] = newsudo
