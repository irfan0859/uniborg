from telethon import events
import os
import requests

ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY")

@borg.on(events.NewMessage(pattern=r".screencapture (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}"
    input_str = event.pattern_match.group(1)
    response_api = requests.get(sample_url.format(ACCESS_KEY, input_str), stream=True)
    temp_file_name = "screenshotlayer.png"
    with open(temp_file_name, "wb") as fd:
        for chunk in response_api.iter_content(chunk_size=128):
            fd.write(chunk)
    try:
        await borg.send_file(
            event.chat_id,
            temp_file_name,
            caption=input_str,
            force_document=True,
            reply_to=event.message.reply_to_msg_id
        )
        await event.delete()
    except:
        await event.edit(response_api.text)
    os.remove(temp_file_name)
