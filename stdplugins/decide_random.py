from telethon import events
import random, re

@borg.on(events.NewMessage(pattern=r"\.decide", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    r = random.randint(1, 100)
    if r % 3 == 1:
        await event.edit("Yes")
    elif r % 3 == 2:
        await event.edit("No")
    else:
        await event.edit("¯\_(ツ)_/¯")
