import sys

import telethon.utils

from userbot import BOT_VER as version
from userbot import (
    DEFAULT,
    DEVS,
    LOGS,
    ROSE2,
    ROSE3,
    ROSE4,
    ROSE5,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_SESSION,
    bot,
    call_py,
)
from userbot.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nRose-Userbot V {}, Copyright © 2021-2022 SendiAp <https://github.com/SendiAp/Rose-Userbot>"
MSG_BLACKLIST = "Terjadi Kesalahan Terhadap, USERBOT {} Atau Mungkin Userbot Di shutdown.\nRose-Userbot V {}, Copyright © 2021-2022 SendiAp <https;//github.com/SendiAp/Rose-Userbot>"

async def rose_client(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


def multirose():
    if 1307579425 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001459812644 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 1307579425 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            bot.loop.run_until_complete(rose_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklistrose:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            print(e)

    if STRING_2:
        try:
            ROSE2.start()
            ROSE2.loop.run_until_complete(rose_client(ROSE2))
            user = ROSE2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistrose:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            print(e)

    if STRING_3:
        try:
            ROSE3.start()
            ROSE3.loop.run_until_complete(rose_client(ROSE3))
            user = ROSE3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistrose:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            print(e)

    if STRING_4:
        try:
            ROSE4.start()
            ROSE4.loop.run_until_complete(rose_client(ROSE4))
            user = ROSE4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistrose:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            print(e)

    if STRING_5:
        try:
            ROSE5.start()
            ROSE5.loop.run_until_complete(rose_client(ROSE5))
            user = ROSE5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistrose:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            print(e)

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    return failed
