from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client,message):
		print(message.chat.id)
		thumb = find(int(message.chat.id))[0]
		if thumb :
			await client.send_photo(message.chat.id,photo =f"{thumb}")
		else:
			await message.reply_text("ʏᴏᴜ  ᴅᴏɴᴛ😐  ʜᴀᴠᴇ  ᴀɴʏ  ᴛʜᴜᴍʙɴᴀɪʟ  ᴛᴏ  ᴠɪᴇᴡ👀 \n\nsᴇɴᴅ  ᴀ  ᴘɪᴄᴛᴜʀᴇ🖼️  ᴛᴏ  sᴇᴛ  ᴀs  ᴀ  ᴛʜᴜᴍʙɴᴀɪʟ")
	
	
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client,message):
	delthumb(int(message.chat.id))
	await message.reply_text("**ʏᴏᴜʀ  ᴄᴜsᴛᴏᴍ  🎑ᴛʜᴜᴍʙɴᴀɪʟ  ᴡᴀs  ᴅᴇʟᴇᴛᴇᴅ✂️ \n\nғʀᴏᴍ  ɴᴏᴡ  ᴏɴ  ʏᴏᴜʀ  ⌨️ᴇᴅɪᴛᴇᴅ  ғɪʟᴇ  ᴡɪʟʟ  ɴᴏᴛ❌ ʜᴀᴠᴇ  ᴀɴʏ  ᴛʜᴜᴍʙɴᴀɪʟ**")

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
	file_id = str(message.photo.file_id)
	addthumb(message.chat.id , file_id)
	await message.reply_text("**ᴛʜɪs  ᴘɪᴄᴛᴜʀᴇ🎑  ɪs  sᴀᴠᴇᴅ  ᴀs  ᴀ  ᴛʜᴜᴍʙɴᴀɪʟ⌨️  ᴏғ  ʏᴏᴜʀ  ғᴜᴛᴜʀᴇ  ᴇᴅɪᴛ  ғɪʟᴇs✅**")
	
