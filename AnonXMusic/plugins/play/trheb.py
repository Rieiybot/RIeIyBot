import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram import Client, emoji 
from AnonXMusic import app
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ChatPermissions
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters


chat_id = -1001967964536

welcome_photo = "path_to_your_welcome_photo.jpg"


@app.on_message(filters.new_chat_members & filters.group)
async def welcome_new_members(client, message):
    for member in message.new_chat_members:
        await message.reply_photo(welcome_photo, f"نورت الجروب ي قمر {member.first_name}\nاحترم الادمن ولا تسئ اللفط")

@app.on_message(filters.left_chat_member)
async def good_bye(client: Client, message: Message):
	chatid= message.chat.id
	await client.send_message(text=f"- مشيت ليه يوحش يلا بسلامات🥲👋\n│ \n╯  {message.from_user.mention} ",chat_id=chatid)
	
	
	
	
	
	
	
