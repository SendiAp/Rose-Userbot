from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.skyzu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Ehh Lu Mau Tau Gak?**")
    sleep(1)
    await typew.edit("**Sih Skyzu mukanya mirip babi😂**")
    sleep(1)
    await typew.edit("**Ehh Gak Bercanda Deh😁**")
    sleep(1)
    await typew.edit("**Emang Bener Sih Skyzu Mukanya Kaya Babi🙈**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh,Skyzu Kan Ganteng Kaya Artis Korea😄**")
    sleep(1)
    await typew.edit("**Tapi Boong😂**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Skyzu Nangis Minta Balon😂**")
    sleep(1)
    await typew.edit("**Maaf Ya Skyzu Ganteng Bercanda💖**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")
# Create by myself @localheart


@register(outgoing=True, pattern='^.adudin(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Adudin**")
    sleep(1)
    await typew.edit("**Adudin Ganteng Banget**")
    sleep(1)
    await typew.edit("**Boleh Aku minta vps? **")
    sleep(1)
    await typew.edit("**Kan dudin Mukanya Kaya Babi🙈**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh,Dudin Kan Ganteng Kaya Artis Korea😄**")
    sleep(1)
    await typew.edit("**Tapi Boong😂**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Dudin Nangis Minta Balon😂**")
    sleep(1)
    await typew.edit("**Pokoknya Dudin Ganteng Banget**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")
# Create by myself @localheart

CMD_HELP.update({
    "familygeez":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.skyzu` / `.adudin`\
    \n↳ : Untuk Ngatain Skyzu."
})
