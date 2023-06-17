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
        txt=f"""**ʜᴇʟʟᴏ{wish} {message.from_user.first_name } \n
	ᴛʜɪs  ɪs  ᴀ  ғᴀsᴛ⚡  4ɢʙ  ʀᴇɴᴀᴍᴇʀ  ʙᴏᴛ🤖  ᴡɪᴛʜ  ᴍᴜʟᴛɪ  ғᴇᴀᴛᴜʀᴇs . ʏᴏᴜ  ᴄᴀɴ  ᴇᴅɪᴛ🖌️  10  ғɪʟᴇs  sɪᴍᴜʟᴛᴀɴᴏᴜsʟʏ💡 .\n\nsᴇɴᴅ  ғɪʟᴇ  ᴏʀ ᴠɪᴅᴇᴏ  ᴛᴏ  ᴇᴅɪᴛ \n\nᴜsᴇ /about ᴄᴏᴍᴍᴀɴᴅ  ᴛᴏ  ᴄʜᴇᴄᴋ  ᴛʜɪs  ʙᴏᴛs  ғᴇᴀᴛᴜʀᴇs**"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("📐ʜᴏᴡ ᴛᴏ ᴇᴅɪᴛ🔧", url="https://telegra.ph/%CA%9C%E1%B4%8F%E1%B4%A1-%E1%B4%9B%E1%B4%8F-%E1%B4%87%E1%B4%85%C9%AA%E1%B4%9B-%D2%93%C9%AA%CA%9F%E1%B4%87-04-16")],
                                      [InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ🛸", url="https://t.me/F9Devs"),
                                       InlineKeyboardButton("ʜᴇʟᴘ🐶", url='https://t.me/CALLADMIN_beebot')],
                                      [InlineKeyboardButton("⚙️ᴜᴘɢʀᴀᴅᴇ ᴘʟᴀɴ🚀", url='https://cosmofeed.com/vig/64836873e34a7f0020e20832')]
                                      ]))
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "**🙄ᴏʜʜᴏ , ʏᴏᴜʀ  ғʀɪᴇɴᴅ  ɪs  ᴀʟʀᴇᴀᴅʏ  ᴜsɪɴɢ  ᴏᴜʀ  ʙᴏᴛ , 🛡️ᴛʀʏ ᴀɴᴏᴛʜᴇʀ**")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup=InlineKeyboardMarkup(
                                             [[InlineKeyboardButton("📐ʜᴏᴡ ᴛᴏ ᴇᴅɪᴛ🔧", url="https://telegra.ph/%CA%9C%E1%B4%8F%E1%B4%A1-%E1%B4%9B%E1%B4%8F-%E1%B4%87%E1%B4%85%C9%AA%E1%B4%9B-%D2%93%C9%AA%CA%9F%E1%B4%87-04-16")],
                                              [InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ🛸", url="https://t.me/F9Devs"),
                                               InlineKeyboardButton("ʜᴇʟᴘ🐶", url='https://t.me/CALLADMIN_beebot')],
                                             [InlineKeyboardButton("⚙️ᴜᴘɢʀᴀᴅᴇ ᴘʟᴀɴ🚀", url='https://cosmofeed.com/vig/64836873e34a7f0020e20832')]
                                          ]))
            except:
                return
        else:
            await client.send_message(id, "🎉ᴄᴏɴɢʀᴀᴛᴇs ! ʏᴏᴜ ᴡᴏɴ 500 ᴍʙ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ ғʀᴏᴍ ʏᴏᴜʀ ʀᴇғᴇʀᴀʟ \n\nʀᴇғᴇʀ🎟️  ᴀɢᴀɪɴ  ᴛᴏ  ᴡɪɴ😀")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 536870912
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""**
	ʜᴇʟʟᴏ{wish} {message.from_user.first_name }\n\n
	ᴛʜɪs  ɪs  ᴀ  ғᴀsᴛ⚡  4ɢʙ  ʀᴇɴᴀᴍᴇʀ  ʙᴏᴛ🤖  ᴡɪᴛʜ  ᴍᴜʟᴛɪ  ғᴇᴀᴛᴜʀᴇs . ʏᴏᴜ  ᴄᴀɴ  ᴇᴅɪᴛ🖌️  10  ғɪʟᴇs  sɪᴍᴜʟᴛᴀɴᴏᴜsʟʏ💡 .\n\nsᴇɴᴅ  ғɪʟᴇ  ᴏʀ ᴠɪᴅᴇᴏ  ᴛᴏ  ᴇᴅɪᴛ \n\nᴜsᴇ /about ᴄᴏᴍᴍᴀɴᴅ  ᴛᴏ  ᴄʜᴇᴄᴋ  ᴛʜɪs  ʙᴏᴛs  ғᴇᴀᴛᴜʀᴇs**
	""", reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("📐ʜᴏᴡ ᴛᴏ ᴇᴅɪᴛ🔧", url="https://telegra.ph/%CA%9C%E1%B4%8F%E1%B4%A1-%E1%B4%9B%E1%B4%8F-%E1%B4%87%E1%B4%85%C9%AA%E1%B4%9B-%D2%93%C9%AA%CA%9F%E1%B4%87-04-16")],
                                          [InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ🛸", url="https://youtube.com/F9Devs"),
                                           InlineKeyboardButton("ʜᴇʟᴘ🐶", url='https://t.me/CALLADMIN_beebot')],
                                          [InlineKeyboardButton("⚙️ᴜᴘɢʀᴀᴅᴇ ᴘʟᴀɴ🚀", url='https://cosmofeed.com/vig/64836873e34a7f0020e20832')]
                                          ]))
	         



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("**😧ᴅᴜᴇ  ᴛᴏ  ᴏᴠᴇʀʟᴏᴀᴅ  ᴏɴʟʏ  ᴏᴜʀ  ᴄʜᴀɴɴᴇʟ  ᴍᴇᴍʙᴇʀs🕴️ ᴄᴀɴ  ᴜsᴇ  ᴛʜɪs  ʙᴏᴛ🤖\n\nɢᴇᴛ 🗞️ʟᴀᴛᴇsᴛ  ʙᴏᴛs  ᴜᴘᴅᴀᴛᴇs, ɢʀᴏᴡɪɴɢ  ᴛᴜᴛᴏʀɪᴀʟ  ᴇᴛᴄ. ᴊᴏɪɴ👇🏻 &  sᴇɴᴅ  ғɪʟᴇ  ᴀɢᴀɪɴ💣**",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ  ᴄʜᴀɴɴᴇʟ🛸" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       try:
           bot_data = find_one(int(botid))
           prrename = bot_data['total_rename']
           prsize = bot_data['total_size']
           user_deta = find_one(user_id)
       except:
           await message.reply_text("**ɪғ  ʏᴏᴜ  ᴀʀᴇ  sᴇᴇɴ  ᴛʜɪs . ᴛʜᴇɴ  ʙᴏᴛ  ɪs  ᴏᴠᴇʀʟᴏᴀᴅᴇᴅ🤥 . \n\nᴋɪɴᴅʟʏ  ᴅᴏ  ᴛʜᴇ  ᴘʀᴏᴄᴇss  ɢɪᴠᴇɴ👇🏻  ʙᴇʟᴏᴡ  &  ʀᴇsᴛᴀʀᴛ  ᴛʜᴇ  ʙᴏᴛ. ᴀɴʏ  ʜᴇʟᴘ🐶  ᴛʜᴇɴ  ᴄᴏɴᴛᴀᴄᴛ  ᴛʜᴇ  ᴅᴇᴠᴇʟᴏᴘᴇʀ**")
       try:
       	used_date = user_deta["date"]
       	buy_date= user_deta["prexdate"]
       	daily = user_deta["daily"]
       	user_type = user_deta["usertype"]
       except:
           await message.reply_text("**ᴏᴠᴇʀʟᴏᴀᴅ  ʜᴀs  ʙᴇᴇɴ  ᴄʟᴇᴀʀᴇᴅ  ᴄʟɪᴄᴋ👉🏻 /about**")
           return
           
           
       c_time = time.time()
       
       if user_type=="Free":
           LIMIT = 620
       else:
           LIMIT = 140
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"```**🙂ᴡᴀɪᴛ ⏳{ltime}⌛ ᴛᴏ  ᴇᴅɪᴛ  ᴀɢᴀɪɴ . ғʟᴏᴏᴅ  ᴡᴀɪᴛ🚦 ᴛɪᴍᴇ  ɪs  ʀᴜɴɴɪɴɢ⏲️  ᴛᴏ  ᴘʀᴇᴠᴇɴᴛ  ᴇʀʀᴏʀ👾, ɢʟɪᴛᴄʜ, ᴀɴᴅ  sʟᴏᴡ ⏱️sᴘᴇᴇᴅ**. \n\nɴᴏᴛᴇ - ᴘʀᴇᴍɪᴜᴍ⭐ ᴜsᴇʀs  ɢᴇᴛ  sᴍᴀʟʟ  ᴛɪᴍᴇ⌛ ɢᴀᴘ```",reply_to_message_id = message.id)
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
       		            await message.reply_text(f"""**💡ᴄʜᴏᴏsᴇ , ᴡʜᴀᴛ  ᴅᴏ  ʏᴏᴜ  ᴡᴀɴᴛ  ᴛᴏ  ᴅᴏ  ᴡɪᴛʜ  ᴛʜɪs  ғɪʟᴇ📂** ?\n\n📑ғɪʟᴇ ɴᴀᴍᴇ :- {filename}\n🪧ғɪʟᴇ sɪᴢᴇ :- {humanize.naturalsize(file.file_size)}\n📍ᴅᴄ ɪᴅ :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
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
       		    await message.reply_text(f"""**💡ᴄʜᴏᴏsᴇ , ᴡʜᴀᴛ  ᴅᴏ  ʏᴏᴜ  ᴡᴀɴᴛ  ᴛᴏ  ᴅᴏ  ᴡɪᴛʜ  ᴛʜɪs  ғɪʟᴇ📂** ?\n\n📑ғɪʟᴇ ɴᴀᴍᴇ :- {filename}\n🪧ғɪʟᴇ sɪᴢᴇ :- {filesize}\n📍ᴅᴄ ɪᴅ :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝ʀᴇɴᴀᴍᴇ/ᴄᴏɴᴠᴇʀᴛ",callback_data = "rename"),
       		InlineKeyboardButton("✖️ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]]))
       		
