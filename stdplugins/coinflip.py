from telethon import events
import random, re

@borg.on(events.NewMessage(pattern=r"\.coinflip (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    r = random.randint(1, 100)
    input_str = event.pattern_match.group(1).lower()
    if r % 2 == 1:
        if input_str == "heads":
            await event.edit("The coin landed on: **Heads**. \n You were correct.")
        else:
            await event.edit("The coin landed on: **Heads**. \n You weren't correct, try again ...")
    elif r % 2 == 0:
        if input_str == "tails":
            await event.edit("The coin landed on: **Tails**. \n You were correct.")
        else:
            await event.edit("The coin landed on: **Tails**. \n You weren't correct, try again ...")
    else:
        await event.edit("¯\_(ツ)_/¯")
