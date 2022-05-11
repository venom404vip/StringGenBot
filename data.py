from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Generate String Session", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("SUPPORT", url="https://t.me/IMLUCIFER404"),
         InlineKeyboardButton("DEVELOPER", url="https://t.me/IMLUCIFER404"),
        ],
    ]

    START = """
Hello {},

My name is {},
This is a bot which create string session for your telegram account. This bot is really safe for all account!

Source : [PAID](https://t.me/IMLUCIFER404)
Note : After you create the string session don't send other or your account will be hacked!
    """
