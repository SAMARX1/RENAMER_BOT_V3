"""lokaman"""

from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)

from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))

async def upgrade(bot,update):

	text = """**⭕𝗖𝗛𝗢𝗢𝗦𝗘  𝗔  𝗣𝗟𝗔𝗡⭕**


	**𝗕𝗔𝗦𝗜𝗖🎟️
        Daily Upload limit 10GB
        PRICE = 20₹🇮🇳 MONTHLY**
	
	
	**𝗦𝗨𝗣𝗘𝗥⚡
	Daily Upload limit 50GB
        PRICE = 45₹🇮🇳 MONTHLY**
	
	
	**𝗗𝗜𝗔𝗠𝗢𝗡𝗗💎
	Daily Upload limit 100GB
	access of premium features
	PRICE = 75₹🇮🇳 MONTHLY**


	**FOREIGN USER CONTACT ADMIN**


	CLICK 👇🏻**ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ** BUTTON TO UPGRADE PLAN"""

	keybord = InlineKeyboardMarkup([[ 

        			InlineKeyboardButton("ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ👑 ",url = "https://cosmofeed.com/vig/64836873e34a7f0020e20832")], 

        			[InlineKeyboardButton("ʜᴇʟᴘ💻",url = "https://t.me/CALLADMIN_beebot"),

        			InlineKeyboardButton("ᴄᴀɴᴄᴇʟ🚫",callback_data = "cancel")]])

	await update.message.edit(text = text,reply_markup = keybord)

	

@Client.on_message(filters.private & filters.command(["upgrade"]))

async def upgradecm(bot,message):

	text = """**𝗖𝗛𝗢𝗢𝗦𝗘  𝗔  𝗣𝗟𝗔𝗡**


	**𝗕𝗔𝗦𝗜𝗖🎟️
	Daily  Upload  limit 10GB
        PRICE = 20₹🇮🇳 MONTHLY** 


	**𝗦𝗨𝗣𝗘𝗥⚡
	Daily Upload limit 50GB
        PRICE = 45₹🇮🇳 MONTHLY**


	**𝗗𝗜𝗔𝗠𝗢𝗡𝗗💎
	Daily Upload limit 100GB
	access of premium features
        PRICE = 75₹🇮🇳 MONTHLY**
	
	
	**FOREIGN USER CONTACT ADMIN**

	
	CLICK 👇🏻**ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ** BUTTON TO UPGRADE PLAN """

	keybord = InlineKeyboardMarkup([[ 

        			InlineKeyboardButton("ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ👑",url = "https://cosmofeed.com/vig/64836873e34a7f0020e20832")], 

        			[InlineKeyboardButton("ʜᴇʟᴘ💻",url = "https://t.me/CALLADMIN_beebot"),

        			InlineKeyboardButton("ᴄᴀɴᴄᴇʟ🚫",callback_data = "cancel")]])

	await message.reply_text(text = text,reply_markup = keybord)
