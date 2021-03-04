from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.yunus(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hallo!! Perkenalkan yah Namaku Yunus`")
    sleep(3)
    await typew.edit("`Umurku 19 tahun dan aku sadboy :)`")
    sleep(1)
    await typew.edit("`Dan Aku Tinggal Di Padang Salam kenal yah`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.tolol(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hy Tolol`")
    sleep(3)
    await typew.edit("`Biar Apa Lu Buat Kek Gitu?`")
    sleep(1)
    await typew.edit("`Dasar Tolol Lebay Alay Goblok`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart
