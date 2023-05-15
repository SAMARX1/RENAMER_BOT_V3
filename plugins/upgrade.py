"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**CHOOSE YOUR PREFERRED PLAN**

	
	**BASIC🎟️** 
	Daily  Upload  limit 10GB
	price Rs 15₹🇮🇳/ per Month
	

	**SUPER⚡**
	Daily Upload limit 50GB
	Price Rs 29₹🇮🇳/ per Month

	
	**DIAMOND💎**
	Daily Upload limit 100GB
	Price Rs 59₹🇮🇳/ per Month
	access of premium features 

	
	**FOREIGN USER CONTACT ADMIN**
	
	CLICK 👇🏻**GET PREMIUM** BUTTON TO UPGRADE PLAN"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("GET PREMIUM👑 ",url = "https://cosmofeed.com/vig/6410a3933702d700208ace5b")], 
        			[InlineKeyboardButton("ADMIN👨‍💻",url = "https://t.me/CALLADMIN_beebot"),
        			InlineKeyboardButton("PAYTM",url = "https://cosmofeed.com/vig/6410a3933702d700208ace5b")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**CHOOSE YOUR PREFERRED PLAN**

	
	**BASIC🎟️** 
	Daily  Upload  limit 10GB
	Price Rs 15₹🇮🇳/ per month

	
	**SUPER⚡**
	Daily Upload limit 50GB
	Price Rs 29₹🇮🇳/ per Month

	
	**DIAMOND💎**
	Daily Upload limit 100GB
	Price Rs 59₹🇮🇳/ per Month
	access of premium features 
	
	**FOREIGN USER CONTACT ADMIN**
	
	CLICK 👇🏻**GET PREMIUM** BUTTON TO UPGRADE PLAN """
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("GET PREMIUM👑",url = "https://cosmofeed.com/vig/6410a3933702d700208ace5b")], 
        			[InlineKeyboardButton("ADMIN👨‍💻",url = "https://t.me/CALLADMIN_beebot"),
        			InlineKeyboardButton("PAYTM",url = "https://cosmofeed.com/vig/6410a3933702d700208ace5b")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)



