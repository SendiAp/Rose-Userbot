# Ported By @VckyouuBitch From Geez - Projects
# Copyright © Geez - Projects
# Github Rose Userbot

from youtube_dl import YoutubeDL

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=".yt(a|v|sa|sv) (.*)", disable_errors=True)
async def download_from_youtube_(event):
    opt = event.pattern_match.group(1).lower()
    if opt == "a":
        ytd = YoutubeDL(
            {
                "format": "bestaudio",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp3",
            }
        )
        url = event.pattern_match.group(2).lower()
        if not url:
            return await event.edit("✋ `Beri saya URL (youtube) untuk mengunduh audio Dari URL kamu!`")
        try:
            request.get(url)
        except BaseException:
            return await event.edit("📂 `Berikan Tautan Audio Langsung Untuk Mengunduh..`")
        xx = await event.edit(get_string("com_1"))
    elif opt == "v":
        ytd = YoutubeDL(
            {
                "format": "best",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp4",
            }
        )
        url = event.pattern_match.group(2).lower()
        if not url:
            return await event.edit("✋ `Beri saya URL (youtube) untuk mengunduh video dari URL kamu!`")
        try:
            request.get(url)
        except BaseException:
            return await event.edit("📂 `Berikan Tautan Video Langsung Untuk Mengunduh...`")
        xx = await event.edit(get_string("com_1"))
    elif opt == "sa":
        ytd = YoutubeDL(
            {
                "format": "bestaudio",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp3",
            }
        )
        try:
            query = event.text.split(" ", 1)[1]
        except IndexError:
            return await event.edit("✋ `Beri saya kueri penelusuran (youtube) untuk mengunduh audio dari URL Kamu!`"
                                    )
        xx = await event.edit("🔍`Mencari di YouTube...`")
        url = await get_yt_link(query)
        await xx.edit("💨 `Mengunduh lagu audio...`")
    elif opt == "sv":
        ytd = YoutubeDL(
            {
                "format": "best",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp4",
            }
        )
        try:
            query = event.text.split(" ", 1)[1]
        except IndexError:
            return await event.edit("Beri saya permintaan pencarian (youtube) untuk mengunduh video dari Pencarian kamu!"
                                    )
        xx = await event.edit("🔍`Mencari di YouTube...`")
        url = await get_yt_link(query)
        await xx.edit("💨 `Mengunduh videi audio...`")
    else:
        return
    await download_yt(xx, event, url, ytd)


CMD_HELP.update(
    {
        "zipfile": "**✘ Plugin** `ytdownload` :\
        \n\n  •  **Perintah :** `.yta` [**Link Youtube**]\
        \n  •  **Fungsi : **Unduh Audio Dari Tautan.\
        \n\n  •  **Perintah :** `.ytv` [**Link Youtube**]\
        \n  •  **Fungsi : **Unduh Video Dari Tautan.\
        \n\n  •  **Perintah :** `.ytsa` [**Permintaan Pencarian Youtube**]\
        \n  •  **Fungsi : **Cari Dan Unduh Audio Dari Youtube.\
        \n\n  •  **Perintah :** `.ytsv` [**Permintaan Pencarian Youtube**]\
        \n  •  **Fungsi : **Cari Dan Unduh Video Dari youtube.\
    "
    }
)
