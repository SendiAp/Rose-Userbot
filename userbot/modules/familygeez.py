from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.vicky(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Ehh Lu Mau Tau Gak?**")
    sleep(1)
    await typew.edit("**Sih Vicky Kan Mukanya Kaya Babi😂**")
    sleep(1)
    await typew.edit("**Ehh Gak Bercanda Deh😁**")
    sleep(1)
    await typew.edit("**Emang Bener Sih Vicky Mukanya Kaya Babi🙈**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh,Vicky Kan Ganteng Kaya Artis Korea😄**")
    sleep(1)
    await typew.edit("**Tapi Boong😂**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Vicky Nangis Minta Balon😂**")
    sleep(1)
    await typew.edit("**Maaf Ya Vicky Ganteng Bercanda💖**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")
# Create by myself @localheart

CMD_HELP.update({
    "familygeez":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vicky`\
    \n↳: Untung Ngatain Vicky."
})
