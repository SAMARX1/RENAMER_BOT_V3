from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("SHARE REFERAL🚀" ,url=f"https://t.me/share/url?url=https://t.me/Thumbnail_editor_4gb_bot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"🤯sʜᴀʀᴇ ᴛʜɪs ʙᴏᴛ ᴡɪᴛʜ ғʀɪᴇɴᴅs🍳 ᴀɴᴅ ɢᴇᴛ ᴜᴘᴛᴏ 5ɢʙ💥 ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ / ᴘᴇʀ ʀᴇғᴇʀᴀʟ \n\n👇🏻ʜᴇʀᴇ ʏᴏᴜʀ 🎟️ʀᴇғᴇʀᴀʟ ᴄᴏᴅᴇ👇🏻",reply_to_message_id = message.id,reply_markup=reply_markup,)
    
