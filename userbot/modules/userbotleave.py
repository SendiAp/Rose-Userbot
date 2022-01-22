import asyncio

from userbot import SUDO_USERS
from userbot.events import register


@register(outgoing=True, pattern=r"^.leavell(?: |$)(.*)")
async def leavell(event):
    if event.from_user.id in SUDO_USERS:
        left = 0
        failed = 0
        await event.edit("Meninggalkan semua obrolan...")
        async for dialog in SUDO_USERS.iter_dialogs():
            try:
                await SUDO_USERS.leave_chat(dialog.chat.id)
                left = left + 1
                await event.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            except BaseException:
                failed = failed + 1
                await event.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await event.send_message(event.chat.id, f"Left {left} chats. Failed {failed} chats.")