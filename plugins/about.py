import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"⚡ᴠᴇʀsɪᴏɴ:6.3 \n⚡ᴜᴘᴅᴀᴛᴇᴅ ᴏɴ 2023/05/15 \n\n**💡ᴛʀʏ  ᴍᴏʀᴇ  ғᴇᴀᴛᴜʀᴇs👇🏻 \n\n🚀𝘕𝘖𝘙𝘔𝘈𝘓  𝘍𝘌𝘈𝘛𝘜𝘙𝘌𝘚👇🏻 \n📌ʀᴇɴᴀᴍᴇ  ғɪʟᴇ  ᴏʀ  ᴠɪᴅᴇᴏ \n📌sᴇᴛ  ᴀᴜᴛᴏ  ᴄᴀᴘᴛɪᴏɴ \n📌sᴇᴛ  ᴛʜᴜᴍʙɴᴀɪʟ \n📌ғɪʟᴇ/ᴠɪᴅᴇᴏ  ᴄᴏɴᴠᴇʀᴛᴇʀ \n\n🚀𝘗𝘙𝘌𝘔𝘐𝘜𝘔  𝘍𝘌𝘈𝘛𝘜𝘙𝘌𝘚👇🏻  \n📌4ɢʙ  ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ \n📌ᴠɪᴅᴇᴏ  ᴛʀɪᴍ  ᴀɴᴅ  ᴍᴇʀɢᴇ \n📌ᴀᴜᴅɪᴏ  ᴄʜᴀɴɢᴇ  ᴏʀ  ʀᴇᴍᴏᴠᴇ \n📌3x  ᴅᴏᴡɴʟᴏᴀᴅ  sᴘᴇᴇᴅ \n\n📦/upgrade  ᴘʟᴀɴ  ᴛᴏ  ᴜsᴇ  ᴘʀᴇᴍɪᴜᴍ  ғᴇᴀᴛᴜʀᴇs**",quote=True)
