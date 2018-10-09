from telethon import events
import os
import requests
import json


@borg.on(events.NewMessage(pattern=r".isup (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/up/{}?sslverify=1".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api == 200:
        await event.edit(input_str + " is online.")
    else:
        await event.edit("i can't seem to find {} on the internet".format(input_str))


@borg.on(events.NewMessage(pattern=r".dns (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("DNS records of {} are \n{}".format(input_str, response_api))
    else:
        await event.edit("i can't seem to find {} on the internet".format(input_str))


@borg.on(events.NewMessage(pattern=r".url (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("Generated {} for {}.".format(response_api, input_str))
    else:
        await event.edit("something is wrong. please try again later.")
