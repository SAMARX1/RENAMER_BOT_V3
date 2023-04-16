import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.progress import humanbytes

from helper.database import  insert ,find_one,used_limit,usertype,uploadlimit,addpredata,total_rename,total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import add_date ,check_expi
CHANNEL = os.environ.get('CHANNEL',"")
import datetime
from datetime import date as date_
LAZY_PIC = os.environ.get("LAZY_PIC","")
STRING = os.environ.get("STRING","")
log_channel = int(os.environ.get("LOG_CHANNEL",""))
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]

#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
	wish = "👋"
elif 12 <= currentTime.hour < 12:
	wish = '🤙'
else:
	wish = '✌️'

#-------------------------------

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""ʜᴇʟʟᴏ{wish} {message.from_user.first_name } \n
	ᴛʜɪs  ɪs  ᴀ  ғᴀsᴛ⚡  4ɢʙ  ʀᴇɴᴀᴍᴇʀ  ʙᴏᴛ🤖  ᴡɪᴛʜ  ᴍᴜʟᴛɪ  ғᴇᴀᴛᴜʀᴇs . ʏᴏᴜ  ᴄᴀɴ  ᴇᴅɪᴛ🖌️  10  ғɪʟᴇs  sɪᴍᴜʟᴛᴀɴᴏᴜsʟʏ💡 .\n\nsᴇɴᴅ  ғɪʟᴇ  ᴏʀ ᴠɪᴅᴇᴏ  ᴛᴏ  ᴇᴅɪᴛ \n\nᴜsᴇ /FEATURES ᴄᴏᴍᴍᴀɴᴅ  ᴛᴏ  ᴄʜᴇᴄᴋ  ᴛʜɪs  ʙᴏᴛs  ғᴇᴀᴛᴜʀᴇs"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("🖌️HOW TO EDIT", url="https://t.me/LazyDeveloper")],
                                      [InlineKeyboardButton("DEVELOPER🛸", url="https://t.me/F9Devs"),
                                       InlineKeyboardButton("ʜᴇʟᴘ🐶", url='https://cosmofeed.com/vig/6410a3933702d700208ace5b')],
                                      [InlineKeyboardButton("☄️ᴜᴘɢʀᴀᴅᴇ ᴘʟᴀɴ📦", url='https://t.me/MOVIEBEEZ')]
                                      ]))
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "Your Friend is Already Using Our Bot")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup=InlineKeyboardMarkup(
                                             [[InlineKeyboardButton("🖌️HOW TO EDIT", url="https://t.me/LazyDeveloper")],
                                              [InlineKeyboardButton("DEVELOPER🛸", url="https://t.me/F9Devs"),
                                               InlineKeyboardButton("ʜᴇʟᴘ🐶", url='https://cosmofeed.com/vig/6410a3933702d700208ace5b')],
                                             [InlineKeyboardButton("☄️ᴜᴘɢʀᴀᴅᴇ ᴘʟᴀɴ📦", url='https://t.me/MOVIEBEEZ')]
                                          ]))
            except:
                return
        else:
            await client.send_message(id, "🎉ᴄᴏɴɢʀᴀᴛᴇs ! ʏᴏᴜ ᴡᴏɴ 500 ᴍʙ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ ғʀᴏᴍ ʏᴏᴜʀ ʀᴇғᴇʀᴀʟ \n\nʀᴇғᴇʀ🎟️  ᴀɢᴀɪɴ  ᴛᴏ  ᴡɪɴ😀")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 536870912
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""
	ʜᴇʟʟᴏ{wish} {message.from_user.first_name }\n\n
	ᴛʜɪs  ɪs  ᴀ  ғᴀsᴛ⚡  4ɢʙ  ʀᴇɴᴀᴍᴇʀ  ʙᴏᴛ🤖  ᴡɪᴛʜ  ᴍᴜʟᴛɪ  ғᴇᴀᴛᴜʀᴇs . ʏᴏᴜ  ᴄᴀɴ  ᴇᴅɪᴛ🖌️  10  ғɪʟᴇs  sɪᴍᴜʟᴛᴀɴᴏᴜsʟʏ💡 .\n\nsᴇɴᴅ  ғɪʟᴇ  ᴏʀ ᴠɪᴅᴇᴏ  ᴛᴏ  ᴇᴅɪᴛ \n\nᴜsᴇ /FEATURES ᴄᴏᴍᴍᴀɴᴅ  ᴛᴏ  ᴄʜᴇᴄᴋ  ᴛʜɪs  ʙᴏᴛs  ғᴇᴀᴛᴜʀᴇs
	""", reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🖌️HOW TO EDIT", url="https://t.me/LazyDeveloper")],
                                          [InlineKeyboardButton("DEVELOPER🛸", url="https://youtube.com/F9Devs"),
                                           InlineKeyboardButton("ʜᴇʟᴘ🐶", url='https://cosmofeed.com/vig/6410a3933702d700208ace5b')],
                                          [InlineKeyboardButton("☄️ᴜᴘɢʀᴀᴅᴇ ᴘʟᴀɴ📦", url='https://t.me/MOVIEBEEZ')]
                                          ]))
	         



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("😧ʏᴏᴜ  ᴀʀᴇ  ɴᴏᴛ  sᴜʙsᴄʀɪʙᴇᴅ  ᴍʏ  ᴜᴘᴅᴀᴛᴇ🛸  ᴄʜᴀɴɴᴇʟ \nᴊᴏɪɴ  ᴛᴏ  ɢᴇᴛ  ʟᴀᴛᴇsᴛ💖 ғᴇᴀᴛᴜʀᴇs  ᴀɴᴅ  ᴜᴘᴅᴀᴛᴇs ᴏғ  ᴛʜɪs  ʙᴏᴛ . \n\n👇🏻ᴊᴏɪɴ  ᴀɴᴅ  sᴇɴᴅ  ғɪʟᴇ  ᴀɢᴀɪɴ👇🏻",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("UPDATE CHANNEL🛸" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       try:
           bot_data = find_one(int(botid))
           prrename = bot_data['total_rename']
           prsize = bot_data['total_size']
           user_deta = find_one(user_id)
       except:
           await message.reply_text("ɪғ  ʏᴏᴜ  ᴀʀᴇ  sᴇᴇɴ ᴛʜɪs  . ᴛʜᴇɴ  ʙᴏᴛ  ɪs  ɴᴏᴛ  ʀᴇsᴘᴏɴᴅɪɴɢ  ᴘʀᴏᴘᴇʀʟʏ  ᴅᴜᴇ  ᴛᴏ  ᴏᴠᴇʀʟᴏᴀᴅ . \n\nᴋɪɴᴅʟʏ  ᴄʟᴇᴀʀ  ᴀʟʟ  ʜɪsᴛᴏʀʏ  ᴏғ  ʙᴏᴛ  ᴀɴᴅ  ʀᴇsᴛᴀʀᴛ  ᴛʜᴇ  ʙᴏᴛ . ɪғ  sᴀᴍᴇ  ᴇʀʀᴏʀ  ᴘᴏᴘᴜᴘ  ᴀɢᴀɪɴ  ᴛʜᴇɴ  ᴄᴏɴᴛᴀᴄᴛ  ᴛʜᴇ  ᴅᴇᴠᴇʟᴏᴘᴇʀ")
       try:
       	used_date = user_deta["date"]
       	buy_date= user_deta["prexdate"]
       	daily = user_deta["daily"]
       	user_type = user_deta["usertype"]
       except:
           await message.reply_text("database has been Cleared click on /start")
           return
           
           
       c_time = time.time()
       
       if user_type=="Free":
           LIMIT = 600
       else:
           LIMIT = 50
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"```ʏᴏᴜ  ᴀʀᴇ  ᴀ  🙂ғʀᴇᴇ  ᴜsᴇʀ  sᴏ  ᴡᴀɪᴛ ⚠️{ltime}⚠️ ᴛᴏ  ᴇᴅɪᴛ  ᴀɢᴀɪɴ  .  \n\nɢᴇᴛ  ᴘʀᴇᴍɪᴜᴍ⭐  ᴛᴏ  ᴀᴠᴏɪᴅ  ᴛɪᴍᴇ⌛ ʟɪᴍɪᴛ  ᴀɴᴅ  ɢᴇᴛ  ᴍᴏʀᴇ  ғᴇᴀᴛᴜʀᴇs📦```",reply_to_message_id = message.id)
       else:
       		# Forward a single message
           		
       		media = await client.get_messages(message.chat.id,message.id)
       		file = media.document or media.video or media.audio 
       		dcid = FileId.decode(file.file_id).dc_id
       		filename = file.file_name
       		value = 2147483648
       		used_ = find_one(message.from_user.id)
       		used = used_["used_limit"]
       		limit = used_["uploadlimit"]
       		expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
       		if expi != 0:
       			today = date_.today()
       			pattern = '%Y-%m-%d'
       			epcho = int(time.mktime(time.strptime(str(today), pattern)))
       			daily_(message.from_user.id,epcho)
       			used_limit(message.from_user.id,0)			     		
       		remain = limit- used
       		if remain < int(file.file_size):
       		    await message.reply_text(f"Sorry! I can't upload files that are larger than {humanbytes(limit)}. File size detected {humanbytes(file.file_size)}\nUsed Daly Limit {humanbytes(used)} If U Want to Rename Large File Upgrade Your Plan ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upgrade 💰💳",callback_data = "upgrade") ]]))
       		    return
       		if value < file.file_size:
       		    if STRING:
       		        if buy_date==None:
       		            await message.reply_text(f" You Can't Upload More Then {humanbytes(limit)} Used Daly Limit {humanbytes(used)} ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upgrade 💰💳",callback_data = "upgrade") ]]))
       		            return
       		        pre_check = check_expi(buy_date)
       		        if pre_check == True:
       		            await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
       		            total_rename(int(botid),prrename)
       		            total_size(int(botid),prsize,file.file_size)
       		        else:
       		            uploadlimit(message.from_user.id,2147483648)
       		            usertype(message.from_user.id,"Free")
	
       		            await message.reply_text(f'Your Plane Expired On {buy_date}',quote=True)
       		            return
       		    else:
       		          	await message.reply_text("🤍ʏᴏᴜ  ᴀʀᴇ  ɴᴏᴛ  ᴀ  ᴅɪᴀᴍᴏɴᴅ  ᴘʟᴀɴ  ᴜsᴇʀ☹️  sᴏ  ʏᴏᴜ  ᴄᴀɴɴ'ᴛ  ᴜᴘʟᴏᴀᴅ  ғɪʟᴇ  ʙɪɢɢᴇʀ  ᴛʜᴀɴ  2 ɢʙ  .  \n\nsᴜʙsᴄʀɪʙᴇᴅ  ᴅɪᴀᴍᴏɴᴅ💎 ᴘʟᴀɴ  ᴛᴏ  ᴜᴘʟᴏᴀᴅ ᴜᴘᴛᴏ🔥  4ɢʙ  ᴀɴᴅ  ɢᴇᴛ  ᴍᴏʀᴇ  ғᴇᴀᴛᴜʀᴇs📦")
       		          	return
       		else:
       		    if buy_date:
       		        pre_check = check_expi(buy_date)
       		        if pre_check == False:
       		            uploadlimit(message.from_user.id,2147483648)
       		            usertype(message.from_user.id,"Free")
       		        
       		    filesize = humanize.naturalsize(file.file_size)
       		    fileid = file.file_id
       		    total_rename(int(botid),prrename)
       		    total_size(int(botid),prsize,file.file_size)
       		    await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),
       		InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
       		
