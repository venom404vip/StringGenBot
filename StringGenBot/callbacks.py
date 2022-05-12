import traceback
from data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from StringGenBot.generate import generate_session, ask_ques, buttons_ques


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user.mention
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
    elif query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await callback_query.answer("𝗧𝗵𝗲 𝗽𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝘃𝟮 𝗼𝗻𝗹𝘆 𝘄𝗼𝗿𝗸 𝘄𝗶𝘁𝗵 𝗯𝗼𝘁 𝘁𝗵𝗮𝘁 𝗮𝗿𝗲 𝘂𝗽𝗱𝗮𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗲 𝗻𝗲𝘄 𝗽𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝘃𝟮!", show_alert=True)
                await generate_session(bot, callback_query.message)
            elif query == "pyrogram1":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, old_pyro=True)
            elif query == "pyrogram_bot":
                await callback_query.answer("𝗧𝗵𝗲 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗼𝗳 𝗽𝗿𝗼𝗴𝗿𝗮𝗺 𝘃𝟮.", show_alert=True)
                await generate_session(bot, callback_query.message, is_bot=True)
            elif query == "telethon_bot":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


ERROR_MESSAGE = "𝗪𝘁𝗳! 𝗦𝗼𝗺𝗲𝘁𝗵𝗶𝗻𝗴 𝘄𝗲𝗻𝘁 𝘄𝗿𝗼𝗻𝗴. \n\n**𝗘𝗿𝗿𝗼𝗿** : {} " \
            "\n\n**𝗣𝗹𝗲𝗮𝘀𝗲 𝗳𝗼𝗿𝘄𝗮𝗿𝗱 𝘁𝗵𝗶𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘁𝗼 @𝗜𝗠𝗟𝗨𝗖𝗜𝗙𝗘𝗥𝟰𝟬𝟰**, 𝗜𝗳 𝘁𝗵𝗶𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 " \
            "𝗗𝗼𝗲𝘀𝗻'𝘁 𝗰𝗼𝗻𝘁𝗮𝗶𝗻 𝗮𝗻𝘆 𝘀𝗲𝗻𝘀𝗶𝘁𝗶𝘃𝗲 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 " \
            "𝗕𝗲𝗰𝗮𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗲𝗿𝗿𝗼𝗿 𝗶𝘀 **𝗡𝗼𝘁 𝗹𝗼𝗴𝗴𝗲𝗱 𝗯𝘆 𝘁𝗵𝗲 𝗯𝗼𝘁** !"
