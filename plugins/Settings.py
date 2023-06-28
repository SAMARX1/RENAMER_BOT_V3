from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.private & filters.command(["settings"]))
async def start(client, message):
	
	reply_markup = InlineKeyboardMarkup([
		[InlineKeyboardButton('THUMBNAIL SETTINGS', callback_data='thumbnail_settings')],
		[
			InlineKeyboardButton('CAPTION SETTINGS', 'caption_settings'),
			InlineKeyboardButton('OTHERS FEATURES', 'others_features')
		],
		[InlineKeyboardButton('CLOSE', 'close_settings')]
	])
	
	await message.reply_text(
		'**'
		'SETTINGS -\n\n'
		'CLICK ON BELOW BUTTONS TO EXPLORE BOT\'S FEATURES.'
		'**',
		reply_markup=reply_markup,
		quote=True
	)
