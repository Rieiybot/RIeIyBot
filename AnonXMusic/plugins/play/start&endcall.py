import asyncio
from pyrogram import Client, filters
from strings import get_command
from pyrogram.types import *
from AnonXMusic import app
from pyrogram.enums import ParseMode


@Client.on_message(filters.video_chat_started)
async def brah(client: Client, message):
    await message.reply("**♪ تم بدا المحادثه الصوتيه 💎 .**")

@Client.on_message(filters.video_chat_ended)
async def brah2(client: Client, message):
    await message.reply("**♪ تم انهاء المحادثه الصوتيه 💎 .**")

@Client.on_message(filters.video_chat_members_invited)
async def fuckoff(client: Client, message):
    text = f"♪ قام : {message.from_user.mention} 💎 .\n"
    x = 0
    for user in m.video_chat_members_invited.users:
        try:
            text += f"♪ بدعوة -> {user.mention} 💎 .\n♪ إلي المحادثة المرئية 💎 ."
            x += 1
        except Exception:
            pass
    try:
        await m.reply(f"**{text}**", reply_to_message_id=m.message_id)
    except:
        pass
