import os 
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup)
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
ADMIN = int(os.environ.get("ADMIN", ""))

from helper.database import botdata, find_one, total_user,getid

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["usersbase"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	id = str(getid())
	ids = id.split(',')

	await message.reply_text(f"⚡️ᴛᴏᴛᴀʟ ᴜsᴇʀs:- {total_user()}\n\n⚡️ᴛᴏᴛᴀʟ ʀᴇɴᴀᴍᴇᴅ ғɪʟᴇs:- {total_rename}\n\n⚡sɪᴢᴇ ᴏғ ʀᴇɴᴀᴍᴇᴅ ғɪʟᴇs:- {humanbytes(int(total_size))}",quote=True,
                             reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton("🦋 Close Menu 🦋", callback_data="cancel")]]) 
                             )
