from data import Data
from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)


ask_ques = "**𝗣𝗹𝗲𝗮𝘀𝗲 𝗰𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗶𝗰𝗵 𝘀𝘁𝗿𝗶𝗻𝗴 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲 :**"
buttons_ques = [
    [
        InlineKeyboardButton("𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠", callback_data="pyrogram1"),
        InlineKeyboardButton("𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗩𝟮", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗕𝗢𝗧", callback_data="pyrogram_bot"),
        InlineKeyboardButton("𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡 𝗕𝗢𝗧", callback_data="telethon_bot"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡"
    else:
        ty = "𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠"
        if not old_pyro:
            ty += " 𝗩𝟮"
    if is_bot:
        ty += " 𝗕𝗢𝗧"
    await msg.reply(f"𝗧𝗿𝘆𝗶𝗻𝗴 𝘁𝗼 𝘀𝘁𝗮𝗿𝘁 **{ty}** 𝘀𝘁𝗿𝗶𝗻𝗴 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝘀𝘁𝗿𝗶𝗻𝗴 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴...\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝘆𝗼𝘂𝗿 **𝗔𝗣𝗜_𝗜𝗗** 𝘁𝗼 𝗽𝗿𝗼𝗰𝗲𝗲𝗱.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply("**𝗔𝗣𝗜_𝗜𝗗** 𝗠𝘂𝘀𝘁 𝗯𝗲 𝗮𝗻 𝗶𝗻𝘁𝗲𝗴𝗲𝗿, 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝘆𝗼𝘂𝗿 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻...", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, "𝗡𝗼𝘄 𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗺𝗲 𝘆𝗼𝘂𝗿 **𝗔𝗣𝗜_𝗛𝗔𝗦𝗛** 𝘁𝗼 𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴...", filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "𝗦𝗲𝗻𝗱 𝗺𝗲 𝘆𝗼𝘂𝗿 **𝗣𝗛𝗢𝗡𝗘_𝗡𝗨𝗠𝗕𝗘𝗥** 𝘄𝗶𝘁𝗵 𝗰𝗼𝘂𝗻𝘁𝗿𝘆 𝗰𝗼𝗱𝗲.\n𝗘𝗫𝗔𝗠𝗣𝗟𝗘 : `+𝟭𝟬𝟬𝟬𝟬𝟬𝟬𝟬𝟬𝟬𝟬`'"
    else:
        t = "𝗦𝗲𝗻𝗱 𝗺𝗲 𝘆𝗼𝘂𝗿 **𝗕𝗢𝗧_𝗧𝗢𝗞𝗘𝗡** 𝘁𝗼 𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲.\n𝗘𝗫𝗔𝗠𝗣𝗟𝗘 : `𝟱𝟰𝟯𝟮𝟭𝟵𝟴𝟳𝟲𝟱:𝗮𝗯𝗰𝗱𝗮𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀𝘁𝗲𝗿𝗮𝗯𝗮𝗮𝗽𝗹𝗼𝗹`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("𝗧𝗿𝘆𝗶𝗻𝗴 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗢𝗧𝗣 𝗮𝘁 𝘁𝗵𝗲 𝗴𝗶𝘃𝗲𝗻 𝗻𝘂𝗺𝗯𝗲𝗿...")
    else:
        await msg.reply("𝗧𝗿𝘆𝗶𝗻𝗴 𝘁𝗼 𝗹𝗼𝗴𝗶𝗻 𝘃𝗶𝗮 𝗯𝗼𝘁 𝘁𝗼𝗸𝗲𝗻...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("𝗬𝗼𝘂𝗿 **𝗔𝗣𝗜_𝗜𝗗** 𝗮𝗻𝗱 **𝗔𝗣𝗜_𝗛𝗔𝗦𝗛** 𝗰𝗼𝗺𝗯𝗶𝗻𝗮𝘁𝗶𝗼𝗻 𝗱𝗼𝗲𝘀𝗻'𝘁 𝗺𝗮𝘁𝗰𝗵 𝘄𝗶𝘁𝗵 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝘀𝘆𝘀𝘁𝗲𝗺.\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("𝗧𝗵𝗲 **𝗣𝗛𝗢𝗡𝗘_𝗡𝗨𝗠𝗕𝗘𝗥** 𝘆𝗼𝘂'𝘃𝗲 𝘀𝗲𝗻𝘁 𝗱𝗼𝗲𝘀𝗻'𝘁 𝗯𝗲𝗹𝗼𝗻𝗴 𝘁𝗼 𝗮𝗻𝘆 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗮𝗰𝗰𝗼𝘂𝗻𝘁.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝘁𝗵𝗲 **𝗢𝗧𝗣** 𝘁𝗵𝗮𝘁 𝘆𝗼𝘂'𝘃𝗲 𝗿𝗲𝗰𝗲𝗶𝘃𝗲𝗱 𝗳𝗿𝗼𝗺 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗼𝗻 𝘆𝗼𝘂𝗿 𝗮𝗰𝗰𝗼𝘂𝗻𝘁.\n𝗜𝗳 𝗢𝗧𝗣 𝗶𝘀 `𝟭𝟮𝟯𝟰𝟱`, **𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗶𝘁 𝗮𝘀** `𝟭 𝟮 𝟯 𝟰 𝟱`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("𝗧𝗶𝗺𝗲 𝗹𝗶𝗺𝗶𝘁 𝗿𝗲𝗮𝗰𝗵𝗲𝗱 𝗼𝗳 𝟭𝟬 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("𝗧𝗵𝗲 𝗢𝗧𝗣 𝘆𝗼𝘂'𝘃𝗲 𝘀𝗲𝗻𝘁 𝗶𝘀 **𝗪𝗥𝗢𝗡𝗚.**\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("𝗧𝗵𝗲 𝗢𝗧𝗣 𝘆𝗼𝘂'𝘃𝗲 𝘀𝗲𝗻𝘁 𝗶𝘀 **𝗘𝗫𝗣𝗜𝗥𝗘𝗗.**\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 **𝗧𝗪𝗢 𝗦𝗧𝗘𝗣 𝗩𝗘𝗥𝗜𝗙𝗜𝗖𝗔𝗧𝗜𝗢𝗡** 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝘁𝗼 𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("𝗧𝗶𝗺𝗲 𝗹𝗶𝗺𝗶𝘁 𝗿𝗲𝗮𝗰𝗵𝗲𝗱 𝗼𝗳 𝟱 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("𝗧𝗵𝗲 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝘆𝗼𝘂'𝘃𝗲 𝘀𝗲𝗻𝗱 𝗶𝘀 𝘄𝗿𝗼𝗻𝗴.\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**𝗧𝗵𝗶𝘀 𝗶𝘀 𝘆𝗼𝘂𝗿 {ty} 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻** \n\n`{string_session}` \n\n**𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘𝗗 𝗕𝗬: @𝗺𝗮𝗸𝗲𝘀𝘁𝗿𝗶𝗻𝗴𝗴𝗲𝗻𝗯𝗼𝘁\n**𝗡𝗼𝘁𝗲 :** 𝗗𝗼 𝗻𝗼𝘁 𝘀𝗵𝗮𝗿𝗲 𝘁𝗵𝗲 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗼𝗿 𝘆𝗼𝘂𝗿 𝗮𝗰𝗰𝗼𝘂𝗻𝘁 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗵𝗮𝗰𝗸𝗲𝗱!"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 𝘆𝗼𝘂𝗿 {} 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻.\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗰𝗵𝗲𝗰𝗸 𝘆𝗼𝘂𝗿 𝘀𝗮𝘃𝗲 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘁𝗼 𝗴𝗲𝘁 𝘁𝗵𝗲 𝘀𝘁𝗿𝗶𝗻𝗴.! \n\n**𝗦𝘁𝗿𝗶𝗻𝗴 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿 𝗯𝗼𝘁 𝗯𝘆** @𝗜𝗠𝗟𝗨𝗖𝗜𝗙𝗘𝗥𝟰𝟬𝟰".format("𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡" if telethon else "𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**𝗖𝗮𝗻𝗰𝗲𝗹𝗹𝗲𝗱 𝘁𝗵𝗲 𝗼𝗻𝗴𝗼𝗶𝗻𝗴 𝘀𝘁𝗿𝗶𝗻𝗴 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗽𝗿𝗼𝗰𝗲𝘀𝘀!**", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗿𝗲𝘀𝘁𝗮𝗿𝘁𝗲𝗱 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 𝗳𝗼𝗿 𝘆𝗼𝘂!**", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**𝗖𝗮𝗻𝗰𝗲𝗹𝗹𝗲𝗱 𝘁𝗵𝗲 𝗼𝗻𝗴𝗼𝗶𝗻𝗴 𝘀𝘁𝗿𝗶𝗻𝗴 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗽𝗿𝗼𝗰𝗲𝘀𝘀!**", quote=True)
        return True
    else:
        return False
