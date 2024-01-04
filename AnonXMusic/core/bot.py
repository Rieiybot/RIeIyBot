from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info(f"يتم تشغيل البوت...")
        super().__init__(
            name="AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>𖤍 تم دخول عالم الادميلار :</u></b>\n\n<b>اذا وجهتك مشكله كم بتواصل مع جروب الدمعم</b>\n\n<b>جروب الدعم : @AlaDmiLAr</b> ",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "البوت لا يستطع الوصول للجروب او القناة السجل تاكد انك رفع البوت و المساعد مشرف ."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"فشل البوت في في الوصول ل مجموعة او قنات السجل\n  بسبب : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "يرجي رفع البوت و المساعد ادمن في جروب او قناة السجل."
            )
            exit()
        LOGGER(__name__).info(f"تم تشغييل {self.name} علي سورس افاتاࢪ")

    async def stop(self):
        await super().stop()
