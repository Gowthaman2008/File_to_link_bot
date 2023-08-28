# This file is a part of TG-FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


class Language(object):
    def __new__ (self, message: Message):
        if getattr(message.from_user, 'language_code', 'Unknown') in self.available:
            return getattr(self, getattr(message.from_user, 'language_code', self.en), self.en)
        else:
            return self.en

    available=['en', 'Test']

    class en(object):
        START_TEXT = """
<b>Hᴇʟʟᴏ👋 {}\n
ɪ Aᴍ Pᴏᴡᴇʀꜰᴜʟʟ Fɪʟᴇ Tᴏ + Sʜᴏʀᴛɴᴇʀ Lɪɴᴋ Aɴᴅ Sᴛᴏʀᴀɢᴇ Bᴏᴛ Iɴ 4GB.\n
Wᴀʀɴɪɴɢ ⚠
Nsғᴡ Rᴇsᴛʀɪᴄᴛᴇᴅ 🚫 Bʀᴇᴀᴋɪɴɢ Rᴜʟᴇs Lᴇᴀᴅs Yᴏᴜ Tᴏ Pᴇʀᴍᴀɴᴇɴᴛ Bᴀɴ\n
💥 Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :<a href='https://t.me/GM_Botzz'>Gᴍ Bᴏᴛᴢᴢ™</a></b>"""

        HELP_TEXT = """
<i>- Sᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.</i>
<i>- I ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴇxᴛᴇʀɴᴀʟ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ !.</i>
<i>- ᴅᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ Wɪᴛʜ Fᴀsᴛᴇsᴛ Sᴘᴇᴇᴅ</i>
<u>🔸 𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u>\n
<b>🔞 Pᴏʀɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</b>\n
<i>Cᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ (ᴏʀ) ʀᴇᴘᴏʀᴛ ʙᴜɢꜱ</i> <b>: <a href='https://t.me/KingOfFondness'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>"""

        ABOUT_TEXT = """
⌬<b><i>𝔸𝕓𝕠𝕦𝕥 𝕄𝕖 ✨</i></b>\n\n
╭<b>🍁 Mʏ ɴᴀᴍᴇ : 𝙁𝙞𝙡𝙚 𝙏𝙤 𝙇𝙞𝙣𝙠 𝘽𝙤𝙩</b>\n
├<b>💥 Vᴇʀꜱɪᴏɴ : 1.7.2</b>\n
├<b>🎭 Lᴀꜱᴛ ᴜᴘᴅᴀᴛᴇᴅ : </b>
╰<b>🤖 Owner : [Mikey](https://t.me/KingOfFondness)</b>
●<b>𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝘽𝙔: [Gᴍ Bᴏᴛᴢᴢ™](https://t.me/GM_Botzz)</b>\n
"""

        stream_msg_text ="""
⌬<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
╭<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n
├<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n
├<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <i>{}</i>\n
╰<b>🖥WATCH :</b> <i>{}</i>\n\n
●<i><u>𝙋𝙊𝙒𝙀𝙍 𝘽𝙔 𝙂ᴍ 𝘽ᴏᴛᴢᴢ™⚡</u></i>
"""


    class Test(object):
        START_TEXT = """
<i>👋 Hᴇʏ in Russian,</i>{}\n
<i>I'm Telegram Files Streaming Bot As Well Direct Links Generator</i>\n
<i>Cʟɪᴄᴋ ᴏɴ Hᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</i>\n
<i><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>\n
<b>🔞 Pᴏʀɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</b>\n\n
<i><u>𝙋𝙊𝙒𝙀𝙍 𝘽𝙔 𝙂ᴍ 𝘽ᴏᴛᴢᴢ™⚡</u></i>"""

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴇʟᴘ ⚙️', callback_data='help'),
        InlineKeyboardButton('Aʙᴏᴜᴛ 🍿', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ ❌', callback_data='close')
        ],
        [InlineKeyboardButton("Gᴍ Bᴏᴛᴢᴢ™", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ 🎭', callback_data='home'),
        InlineKeyboardButton('Aʙᴏᴜᴛ 🍿', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ ❌', callback_data='close'),
        ],
        [InlineKeyboardButton("Gᴍ Bᴏᴛᴢᴢ™", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ 🎭', callback_data='home'),
        InlineKeyboardButton('Hᴇʟᴘ ⚙️', callback_data='help'),
        InlineKeyboardButton('Cʟᴏsᴇ ❌', callback_data='close'),
        ],
        [InlineKeyboardButton("Gᴍ Bᴏᴛᴢᴢ™", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
