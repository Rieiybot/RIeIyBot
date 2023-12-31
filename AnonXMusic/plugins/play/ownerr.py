import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv

load_dotenv()

OWNER_ID = getenv("OWNER_ID")

OWNER = getenv("OWNER")


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj





@app.on_message(
    filters.command(["مطور", "المطور","مطور البوت"], "")
    & filters.group
  
)
async def huhh(client: Client, message: Message):
    usr = await client.get_users(OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)      
    await message.reply_photo(photo,        caption=f"""⊰•━━﴾ 𖤍 𝗘𝗹𝗔𝗡𝗞𝗔𝗔 𖤍 ﴿━━•⊱\n\n🔥 ¦ ɴᴀᴍᴇ : {usr.first_name}\n🎯 ¦ ᴜѕᴇʀ : @{OWNER}\n🎸 ¦ ɪᴅ : <code>{usr.id}</code>\n\n⊰•━━﴾ 𖤍 𝗘𝗹𝗔𝗡𝗞𝗔𝗔 𖤍 ﴿━━•⊱ """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{OWNER}")
            ],                   
          ]              
       )                 
    )                    
                   
