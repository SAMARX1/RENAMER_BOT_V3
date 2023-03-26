import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["features"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"**💡FEATURES OF THIS BOT👇🏻 \n\n🚀FREE FEATURES \n📌rename file or video \n📌custom caption and thumbnail support \n📌file/video convert \n\n🚀PREMIUM FEATURES \n📌video trim and merge \n📌 audio change and remove \n📌3x download speed \n📌4Gb upload support \n\n📦/UPGRADE PLAN TO USE PREMIUM💥 FEATURES**",quote=True)
