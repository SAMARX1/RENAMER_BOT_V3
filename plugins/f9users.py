import os

from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from helper.database import botdata, find_one, total_user, getid

from helper.progress import humanbytes

token = os.environ.get('TOKEN', '')

botid = token.split(':')[0]

ADMIN = int(os.environ.get('ADMIN', ''))

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command('f9users'))

async def start(client, message):

    data = find_one(int(botid))

    total_rename = data['total_rename']

    total_size = data['total_size']

    await message.reply_text(f'⚡️ Total User: {total_user()}\n\n⚡️ Total Renamed File: {total_rename}\n\n⚡️ Total Size Renamed: {humanbytes(int(total_size))}',

                             quote=True,

                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🦋 Close Menu 🦋', callback_data='cancel')]])

                             )

