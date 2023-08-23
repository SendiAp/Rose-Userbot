import importlib
import time
from pyrogram import idle
from uvloop import install
from roselibs import logging, BOT_VER, __version__ as gver
from Rose import LOGGER, LOOP, aiosession, bot1, bots, app, ids
from config import CMD_HNDLR, BOTLOG_CHATID
from Rose.modules import ALL_MODULES
from userbot.modules.basic.heroku import rose_log


MSG_ON = """
**Rose Userbot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
**Userbot Version -** `{}`
**Geez Library Version - `{}`**
**Ketik** `{}ping` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
©️2023 Rose|Userbot Projects 
"""

async def main():
    await app.start()
    LOGGER("userbot").info("Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Rose.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await logging(bot)
            await rose_log()
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, gver, CMD_HNDLR))
            except BaseException as a:
                LOGGER("userbot").warning(f"{a}")
            LOGGER("userbot").info("Startup Completed")
            LOGGER("userbot").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("userbot").info(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("userbot").info("Starting Rose Userbot")
    install()
    LOOP.run_until_complete(main())
