import asyncio
from pyrogram import Client, filters
from strings import get_command
from pyrogram.types import *
from AnonXMusic import app
from pyrogram.enums import ParseMode



@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("• عندي برد مش قادر اغني 😪🖤")
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
       await message.reply("• قفله ف دماغك يبعيد 🙄🖤")
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"• الراجل دا عايزك ف الكول ← {message.from_user.mention}\n"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
              text = parse_mode = f"{ ParseMode.MARKDOWN }"
              x = 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass  
