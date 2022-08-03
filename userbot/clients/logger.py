# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import ROS2, ROS3, ROS4, ROS5, bot, branch, tgbot
from userbot.utils import checking

MSG_ON = """
Rose-Userbot Sudah Bisa Dipakai 💁
"""


async def man_userbot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            RosUBOT = await tgbot.get_me()
            BOT_USERNAME = RosUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            RosUBOT = await tgbot.get_me()
            BOT_USERNAME = RosUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await checking(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if ROS2:
            await checking(ROS2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await ROS2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if ROS3:
            await checking(ROS3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await ROS3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if ROS4:
            await checking(ROS4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await ROS4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if ROS5:
            await checking(ROS5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await ROS5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
