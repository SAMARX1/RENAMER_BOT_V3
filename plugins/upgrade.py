"""lokaman"""

from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)

from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))

async def upgrade(bot,update):

	text = """**CHOOSE YOUR PREFERRED PLAN**

	

	**BASIC🎟️** 

	Daily  Upload  limit 10GB

	price Rs 20₹🇮🇳/ per Month

	

	**SUPER⚡**

	Daily Upload limit 50GB

	Price Rs 45₹🇮🇳/ per Month

	

	**DIAMOND💎**

	Daily Upload limit 100GB

	Price Rs 75₹🇮🇳/ per Month

	access of premium features 

	

	**FOREIGN USER CONTACT ADMIN**

	

	CLICK 👇🏻**ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ** BUTTON TO UPGRADE PLAN"""

	keybord = InlineKeyboardMarkup([[ 

        			InlineKeyboardButton("ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ👑 ",url = "https://cosmofeed.com/vig/64836873e34a7f0020e20832")], 

        			[InlineKeyboardButton("ʜᴇʟᴘ💻",url = "https://t.me/CALLADMIN_beebot"),

        			InlineKeyboardButton("ᴄᴀɴᴄᴇʟ🚫",callback_data = "cancel")]])

	await update.message.edit(text = text,reply_markup = keybord)

	

@Client.on_message(filters.private & filters.command(["upgrade"]))

async def upgradecm(bot,message):

	text = """**CHOOSE YOUR PREFERRED PLAN**

	

	**BASIC🎟️** 

	Daily  Upload  limit 10GB

	Price Rs 20₹🇮🇳/ per month

	

	**SUPER⚡**

	Daily Upload limit 50GB

	Price Rs 45₹🇮🇳/ per Month

	

	**DIAMOND💎**

	Daily Upload limit 100GB

	Price Rs 75₹🇮🇳/ per Month

	##access of premium features 

	

	**FOREIGN USER CONTACT ADMIN**

	

	CLICK 👇🏻**ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ** BUTTON TO UPGRADE PLAN """

	keybord = InlineKeyboardMarkup([[ 

        			InlineKeyboardButton("ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ👑",url = "https://cosmofeed.com/vig/64836873e34a7f0020e20832")], 

        			[InlineKeyboardButton("ʜᴇʟᴘ💻",url = "https://t.me/CALLADMIN_beebot"),

        			InlineKeyboardButton("ᴄᴀɴᴄᴇʟ🚫",callback_data = "cancel")]])

	await message.reply_text(text = text,reply_markup = keybord)
