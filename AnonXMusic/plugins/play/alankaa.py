import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

                
@app.on_message(
    filters.command(["يا سورس ","سورس","السورس","سورس مين","ادميلار","الادميلار","ي سورس"], "")
    & filters.group
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/eladmilar",
        caption=f"""⊰•━━﴾ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ﴿━━•⊱\n\nمرحبا بك عزيزي {message.from_user.mention} في قسم الادميلار سورس \n\n⊰•━━﴾ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ﴿━━•⊱""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚓️ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ⚓️", url=f"https://t.me/eladmilar"),
                ],[
                    InlineKeyboardButton(
                        "⚓️ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ⚓️", url=f"https://t.me/aladmilar"),
                ],

            ]

        ),

    )







@app.on_message(
    filters.command(["مطورين الادميلار","المطورين","مطورين"], "")
    & filters.group
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/eladmilar",
        caption=f"""⊰•━━﴾ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ﴿━━•⊱\n\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين الاميلار ميوزك\n\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n\n⊰•━━﴾ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ﴿━━•⊱""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚓️ 𝗗𝗘𝗩 ⚓️", url=f"https://t.me/si_i_i"),
                ],[
                
                    InlineKeyboardButton(
                        "⚓️ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ⚓️", url=f"https://t.me/eladmilar"),
                ],

            ]

        ),

    )



@app.on_message(
    filters.command(["بوت جلسات","جلسه","جلسة بايرو","جلسة بايروجرام","بايروجرام","تليثون","تيرمكس","جلسة تليثوت","جلسة تيريمكس","استخراج جلسه","بوت جلسه","بوت جلسة"], "")
    & filters.group
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/glsatbot",
        caption=f"""⊰•━━﴾ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ﴿━━•⊱\n\nمرحبا بك عزيزي {message.from_user.mention} في قسم افضل و ائمن بوت لستخراج الجلسات للميوزك و التليثون\n\n⊰•━━﴾ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ﴿━━•⊱""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "بوت استخراج جلسات 📟", url=f"https://t.me/glsatbot"),
                ],[
                
                    InlineKeyboardButton(
                        "⚓️ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ⚓️", url=f"https://t.me/eladmilar"),
                ],

            ]

        ),

    )




@app.on_message(
    filters.command(["شيكو","شيكوو","المطور شيكو","shikoo","shiko","المطور","مطور","مطور البوت"], "")
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("si_i_i")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"⊰•━━﴾ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ﴿━━•⊱\n\n‍<b>╭⦿ᚐᴅᴇᴠ :</b> {name}\n<b>╰⦿ᚐᴜѕᴇʀ :</b> @{usr.username}\n<b>╭⦿ᚐɪᴅ :</b> <code>{usr.id}</code>\n<b>╰⦿ᚐʙɪᴏ :</b> {usr.bio}\n\n⊰•━━﴾ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ﴿━━•⊱", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    filters.command(["ذكاء","ذكاء اصتناعي","الذكاء الاصطناعي"], "")
    & filters.group
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/eladmilar",
        caption=f"""⊰•━━﴾ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ﴿━━•⊱\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بـ سورس الادميلار\n╮⦿ لتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n╯⦿ بلاك + السؤال بالاسفل 👇\n⊰•━━﴾ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ﴿━━•⊱""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                        "⚓️ 𝗘𝗟𝗔𝗗𝗠𝗜𝗟𝗔𝗥 ⚓️", url=f"https://t.me/eladmilar"),
                ],

            ]

        ),

    )
