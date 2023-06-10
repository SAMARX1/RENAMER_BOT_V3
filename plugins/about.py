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
	await message.reply_text(f"⚡ᴠᴇʀsɪᴏɴ:6.4 \n⚡ᴜᴘᴅᴀᴛᴇᴅ ᴏɴ 2023/06/10 \n\n**ғᴇᴀᴛᴜʀᴇs👇🏻** \n\n📦ʀᴇɴᴀᴍᴇ  ғɪʟᴇs ᴏʀ ᴠɪᴅᴇᴏ 🆓\n📦ᴄᴏɴᴠᴇʀᴛ ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ 🆓\n📦sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ ᴏɴ ᴠɪᴅᴇᴏ 🆓 \n📦sᴇᴛ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ 🆓\n📦4ɢʙ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 👑\n📦3x ᴅᴏᴡɴʟᴏᴀᴅ sᴘᴇᴇᴅ👑\n📦ᴛʀɪᴍ ᴏʀ ᴍᴇʀɢᴇ ᴠɪᴅᴇᴏ 💎\n📦ᴀᴜᴅɪᴏ ᴄʜᴀɴɢᴇ ᴏʀ ʀᴇᴍᴏᴠᴇᴅ 💎\n\n **🆓 = all users can use\n👑 = only premium users can use\n💎 = only DIAMOND users can use**\n\n⚡**/upgrade 𝗣𝗟𝗔𝗡 𝗧𝗢 𝗨𝗦𝗘 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦**",quote=True)
