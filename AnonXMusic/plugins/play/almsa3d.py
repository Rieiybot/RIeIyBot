from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import ASS_MENTION, LOGGER, SUDOERS, app, app2


@app.on_message(filters.command(["asspfp", "setpfp","تغيير صورة المساعد"], "") & SUDOERS)
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("» جاري تغيير صورة المساعد...")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"» تم تغيير صورة المساعد \n│\n╰⦿ᚐ{ASS_MENTION}."
            )
        except:
            return await fuk.edit_text("» فشل تغيير الصوره.")
    else:
        await message.reply_text(
            "» الرجاء الرد علي الصوره المراد وضعها."
        )


@app.on_message(filters.command(["delpfp", "delasspfp","حذف صورة المساعد"], "") & SUDOERS)
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "» تم حذف صورة المساعد بنجاح."
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("» فشل حذف الصوره .")


@app.on_message(filters.command(["assbio", "setbio","تغيير بايو الساعد"], "") & SUDOERS)
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"» تم تغيير بايو المساعد \n│\n╰⦿ᚐ{ASS_MENTION}"
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"» تم تغيير بايو المساعد \n│\n╰⦿ᚐ{ASS_MENTION}")
    else:
        return await message.reply_text(
            "» الرجاء الرد علي البايو المراد وضعه."
        )


@app.on_message(filters.command(["assname", "setname","تغيير اسم المساعد"], "") & SUDOERS)
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"» تم تغيير اسم المساعد \n│\n╰⦿ᚐ{ASS_MENTION} "
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» تم تغيير اسم المساعد \n│\n╰⦿ᚐ{ASS_MENTION}")
    else:
        return await message.reply_text(
            "» الرجاء الرد علي اسم المساعد المراد وضعه."
        )
