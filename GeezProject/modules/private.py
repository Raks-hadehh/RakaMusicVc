# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from GeezProject.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from GeezProject.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME, OWNER
logging.basicConfig(level=logging.INFO)

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Haii {message.from_user.first_name} 𝚂𝙰𝚈𝙰 𝙰𝙳𝙰𝙻𝙰𝙷 {PROJECT_NAME}\n
𝙶𝚄𝙰 𝙸𝚃𝚄 𝙱𝙾𝚃 𝙼𝚄𝚂𝙸𝙲 𝙶𝚁𝙾𝚄𝙿,𝚈𝙰𝙽𝙶 𝙱𝙸𝚂𝙰 𝙼𝙴𝙼𝚄𝚃𝙰𝚁 𝙻𝙰𝙶𝚄 𝙳𝙸 𝙾𝙱𝚁𝙾𝙻𝙰𝙽 𝚂𝚄𝙰𝚁𝙰 𝙶𝚁𝙾𝚄𝙿 𝙻𝙾 𝙳𝙴𝙽𝙶𝙰𝙽 𝙼𝚄𝙳𝙰𝙷 𝙶𝚄𝙰 𝙿𝚄𝙽𝚈𝙰 𝙱𝙰𝙽𝚈𝙰𝙺 𝙵𝙸𝚃𝚄𝚁 : • 𝙼𝙴𝙼𝚄𝚃𝙰𝚁 𝙼𝚄𝚂𝙸𝙲. • 𝙼𝙴𝙽𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝚄𝚂𝙸𝙲. • 𝙼𝙴𝙽𝙲𝙰𝚁𝙸 𝙻𝙰𝙶𝚄 𝚈𝙰𝙽𝙶 𝙻𝙾 𝙼𝙰𝚄 𝙿𝚄𝚃𝙰𝚁 𝙰𝚃𝙰𝚄 𝚈𝙰𝙽𝙶 𝙻𝙾 𝙼𝙰𝚄 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳. • 𝙶𝚄𝙽𝙰𝙺𝙰𝙽 𝙿𝙴𝚁𝙸𝙽𝚃𝙰𝙷 » /help « 𝙱𝙸𝙰𝚁 𝙻𝙾 𝙶𝙰 𝙱𝙴𝙶𝙾

📌 𝙺𝙴𝙽𝙰𝙻𝙸𝙽 𝙽𝙸𝙷 𝚃𝚄𝙰𝙽 𝙶𝚄𝙰  : {OWNER}

Ingin Menambahkan Saya ke Grup Anda? Tambahkan Saya Ke Group Anda!
DAN JANGAN GALAU YA NGENTODD!!!
</b>""",

# Edit Yang Seharusnya Lu Edit Aja:D
# Tapi Jangan di Hapus Special Thanks To nya Yaaa :'D

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝙏𝘼𝙈𝘽𝘼𝙃𝙄𝙉 𝙂𝙐𝘼 𝙆𝙀 𝙂𝙍𝙊𝙐𝙋 𝙇𝙊 ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "💬 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url=f"https://t.me/{UPDATES_CHANNEL}"), 
                    InlineKeyboardButton(
                        "🎈 𝙂𝙧𝙤𝙪𝙥 𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url=f"https://t.me/{SUPPORT_GROUP}")
                ],[
                    InlineKeyboardButton(
                        "📌 𝙅𝙊𝙄𝙉 𝙂𝘾 𝙂𝙐𝘼'", url=f"https://t.me/sinihadehh")
                ],[
                    InlineKeyboardButton(
                        "🔱 𝙏𝙐𝘼𝙉 𝙂𝙐𝘼 𝙉𝙄𝙃 ", url=f"https://t.me/rakaaanjayy")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'Next »', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("➕ Tambahkan saya ke Grup Anda ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '💬 Channel Updates', url=f"https://t.me/isikepalavalen"),
             InlineKeyboardButton(text = '🔰 Group Support', url=f"https://t.me/sinihadehh")],
            [InlineKeyboardButton(text = '🛠 Source Code 🛠', url=f"https://github.com/Raks-hadehh/RakaMusicVc")],
            [InlineKeyboardButton(text = '«', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '«', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '»', callback_data = f"help+{pos+1}")
            ],
        ]
    return button


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Apakah Anda ingin mencari Link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Tidak ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Klik Tombol dibawah untuk Melihat Cara Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 BACA NIH BIAR GA BEGO 📜", url="https://t.me/isikepalavalen/8"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **berhasil dimulai ulang!**\n\n• **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url=f"https://t.me/sinihadehh"
                    ),
                    InlineKeyboardButton(
                        "Created By", url=f"https://t.me/rakaaanjayy"
                    )
                ]
            ]
        )
   )

