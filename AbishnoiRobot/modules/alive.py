import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from AbishnoiRobot.events import register
from AbishnoiRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/c8b388e5c3fa17f7dbbfe.jpg",
    "https://telegra.ph/file/32c5d35031af56a2bc37e.mp4",
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ 「 Aʟɪsʜᴀ 𒆜 ʀᴏʙᴏᴛ 」​**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [ᴅᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/VeNoM_HAi_HuM)** \n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/Abishnoi_ro_bot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/AlishaSupport"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


## Alive mod
