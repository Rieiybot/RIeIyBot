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
    filters.command(["يا سورس ","سورس","السورس"], "")
    & filters.group
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/BIACKB0T",
        caption=f"""⊰•━━﴾ 父 𝗕𝗟𝗔𝗖𝗞 父 ﴿━━•⊱\n\nمرحبا بك عزيزي {message.from_user.mention} في قسم بلاگ بوت\n\n⊰•━━﴾ 父 𝗕𝗟𝗔𝗖𝗞 父 ﴿━━•⊱""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التحديثات", url=f"https://t.me/BIACKB0T"),
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/SI_I_I"),
                ],[
                
                    InlineKeyboardButton(
                        "父 𝗕𝗟𝗔𝗖𝗞 ࿈ 𝗕𝗢𝗧 父", url=f"https://t.me/BIACKB0T"),
                ],

            ]

        ),

    )







@app.on_message(
    filters.command(["مطورين بلاك ","المطورين","مطورين"], "")
    & filters.group
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/BIACKB0T",
        caption=f"""⊰•━━﴾ 父 𝗕𝗟𝗔𝗖𝗞 父 ﴿━━•⊱\n\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين العنقاء ميوزك\n\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n\n⊰•━━﴾ 父 𝗕𝗟𝗔𝗖𝗞 父 ﴿━━•⊱""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ѕʜɪᴋᴏ", url=f"https://t.me/si_i_i"),
                ],[
                
                    InlineKeyboardButton(
                        "父 𝗕𝗟𝗔𝗖𝗞 ࿈ 𝗕𝗢𝗧 父", url=f"https://t.me/BIACKB0T"),
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
        caption=f"""⊰•━━﴾ 父 𝗕𝗟𝗔𝗖𝗞 父 ﴿━━•⊱\n\nمرحبا بك عزيزي {message.from_user.mention} في قسم افضل و ائمن بوت لستخراج الجلسات للميوزك و التليثون\n\n⊰•━━﴾ 父 𝗕𝗟𝗔𝗖𝗞 父 ﴿━━•⊱""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "بوت استخراج جلسات 📟", url=f"https://t.me/glsatbot"),
                ],[
                
                    InlineKeyboardButton(
                        "父 𝗕𝗟𝗔𝗖𝗞 ࿈ 𝗕𝗢𝗧 父", url=f"https://t.me/BIACKB0T"),
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
    await message.reply_photo(photo,       caption=f"⊰•━━﴾ 父 𝗕𝗟𝗔𝗖𝗞 父 ﴿━━•⊱\n\n‍<b>╭⦿ᚐᴅᴇᴠ :</b> {name}\n<b>╰⦿ᚐᴜѕᴇʀ :</b> @{usr.username}\n<b>╭⦿ᚐɪᴅ :</b> <code>{usr.id}</code>\n<b>╰⦿ᚐʙɪᴏ :</b> {usr.bio}\n\n⊰•━━﴾ 父 𝗕𝗟𝗔𝗖𝗞 父 ﴿━━•⊱", 
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
        photo=f"https://telegra.ph/file/a0fe6e57e189cc05e6e05.jpg",
        caption=f"""⊰•━━﴾ 父 𝗕𝗟𝗔𝗖𝗞 父 ﴿━━•⊱\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس العنقاء\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل 👇\n⊰•━━﴾ 父 𝗕𝗟𝗔𝗖𝗞 父 ﴿━━•⊱""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "父 𝗕𝗟𝗔𝗖𝗞 ࿈ 𝗕𝗢𝗧 父", url=f"https://t.me/BIACKB0T"),
                ],

            ]

        ),

    )
