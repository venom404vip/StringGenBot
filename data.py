from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗦𝘁𝗿𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/IMLUCIFER404"),
         InlineKeyboardButton("𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥", url="https://t.me/IMLUCIFER404"),
        ],
    ]

    START = """
𝗛𝗲𝗹𝗹𝗼 {},

𝗠𝘆 𝗻𝗮𝗺𝗲 𝗶𝘀 {},
𝗧𝗵𝗶𝘀 𝗶𝘀 𝗮 𝗯𝗼𝘁 𝘄𝗵𝗶𝗰𝗵 𝗰𝗿𝗲𝗮𝘁𝗲 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗳𝗼𝗿 𝘆𝗼𝘂𝗿 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗮𝗰𝗰𝗼𝘂𝗻𝘁. 𝗧𝗵𝗶𝘀 𝗯𝗼𝘁 𝗶𝘀 𝗿𝗲𝗮𝗹𝗹𝘆 𝘀𝗮𝗳𝗲 𝗳𝗼𝗿 𝗮𝗹𝗹 𝗮𝗰𝗰𝗼𝘂𝗻𝘁!

𝗡𝗼𝘁𝗲 : 𝗔𝗳𝘁𝗲𝗿 𝘆𝗼𝘂 𝗰𝗿𝗲𝗮𝘁𝗲 𝘁𝗵𝗲 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗱𝗼𝗻'𝘁 𝘀𝗲𝗻𝗱 𝗼𝘁𝗵𝗲𝗿 𝗼𝗿 𝘆𝗼𝘂𝗿 𝗮𝗰𝗰𝗼𝘂𝗻𝘁 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗵𝗮𝗰𝗸𝗲𝗱!
    """
