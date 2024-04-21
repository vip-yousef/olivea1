#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @SOURCEOliVEA
#𝙳𝙴𝚅 𝙼𝙰𝚉𝙴𝙽 : @ZzZzZl1l
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @miika3
#Vip MaZeN تم التعديل بواسطة 🎸 ⋅
from pyrogram.types import CallbackQuery
import asyncio
from asyncio import gather
import os
import time
import requests
from pyrogram import enums
from pyrogram import types
import aiohttp
from pyrogram.types import CallbackQuery
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AdRenalen import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AdRenalen import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait



##############################################################
##############################################################
          
     
@app.on_message(filters.command(["سورس","السورس","سورس مين","اوليفيا"], ""), group=221213)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/DEVSOLiVEA/5",
        caption=f"""• [⌯𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄⌯](https://t.me/ZzZzZl1l) •\n
 [⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐎𝑳𝐈𝐕𝐄𝐀⌯](https://t.me/SOURCEOliVEA)\n
 [⌯𝐒𝐔𝐏𝐏𝐔𝐑𝐓.𝐒𝐎𝐔𝐑𝐂𝐄⌯](https://t.me/miika3)\n""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ 𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄 › ", url=f"https://t.me/ZzZzZl1l"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐎𝑳𝐈𝐕𝐄𝐀 ›", url=f"https://t.me/SOURCEOliVEA"), 
                    InlineKeyboardButton(
                        "‹ 𝐒𝐔𝐏𝐏𝐔𝐑𝐓 ›", url=f"https://t.me/miika3"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/V_E_PBot?startgroup=new"),
            ]
        ]
         ),parse_mode=enums.ParseMode.MARKDOWN)



@app.on_message(filters.command(["مازن","ميزو"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/84a08fb44bd1e80baf64f.jpg",
        caption=f"""• ⌯ Developer Name : ˛ 𝙼𝙰𝚉𝙴𝙽 ⌯ •\n- Devloper Username : @ZzZzZl1l Devlopr id : 6816180621 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/SOURCEOliVEA"),
                ],[
                    InlineKeyboardButton(
                        "𓂄𓆩νιρ ʍαzεπ𓆪𓂁", url=f"https://t.me/ZzZzZl1l"), 
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/V_E_PBot?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["المطور","مطور السورس","مزيكا"], ""))
async def deev(client: Client, message: Message):
     if await joinch(message):
            return
     user = await client.get_chat(chat_id="ZzZzZl1l")
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"هناك شخص بالحاجه اليك عزيزي المطور\n{chat_title}\nChat Id : {message.chat.id}",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
       pass
     await message.reply_photo(
     photo=photo,
     caption=f"Developer Name : {name} \nDevloper Username : @{username}\n{bio}",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        passpass
               
        iddof = []
id = {}

@app.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "") & filters.group)
async def iddlock(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in iddof:
            return await message.reply_text("♪ الامر معطل من قبل 💎 .")
        iddof.append(message.chat.id)
        return await message.reply_text("♪ تم تعطيل الايدي بنجاح 💎 .")
    else:
        return await message.reply_text("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط 💎 .")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "") & filters.group)
async def iddopen(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in iddof:
            return await message.reply_text("♪ الايدي مفعل من قبل 💎 .")
        iddof.remove(message.chat.id)
        return await message.reply_text("♪ تم تفعيل الايدي بنجاح 💎 .")
    else:
        return await message.reply_text("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط 💎 .")

@app.on_message(filters.command(["ايدي"], ""))
async def muid(client: Client, message):
    if message.chat.id in iddof:
        return await message.reply_text("♪ تم تعطيل امر الايدي من قبل المشرفين 💎 .")
    
    user = await client.get_chat(message.from_user.id)
    user_id = user.id
    username = user.username
    first_name = user.first_name
    bioo = user.bio
    
    photo = user.photo.big_file_id
    if photo:
        photo = await client.download_media(photo)
    else:
        photo = None
    
    if user.id not in id:
        id[user.id] = []
    
    idd = len(id[user.id])
    
    caption = f"name : {first_name}\nid : {user_id}\nuser : [@{username}]\nbio : {bioo}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")]])
    
    await message.reply_photo(photo=photo, caption=caption, reply_markup=reply_markup)

@app.on_callback_query(filters.regex("heart"))
async def heart(client, query: CallbackQuery):
    callback_data = query.data.strip()
    callback_request = callback_data.replace("heart", "")
    username = int(callback_request)
    usr = await client.get_chat(username)
    
    if usr.id not in id:
        id[usr.id] = []
    
    if query.from_user.mention not in id[usr.id]:
        id[usr.id].append(query.from_user.mention)
    else:
        id[usr.id].remove(query.from_user.mention)
    
    idd = len(id[usr.id])
    
    caption = f"name : {usr.first_name}\nid : {usr.id}\nuser : [@{usr.username}]\nbio : {usr.bio}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{usr.id}")]])
    
    await query.edit_message_text(caption, reply_markup=reply_markup)
        
@app.on_message(filters.command(["اسمي","اسمي اي","قول اسمي"], ""), group=123222)
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""- اسمك » ⦗ {message.from_user.mention} ⦘ 💘 ⋅""") 


##############################################################
##############################################################
##############################################################
  


#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @SOURCEOliVEA
#𝙳𝙴𝚅 𝙼𝙰𝚉𝙴𝙽 : @ZzZzZl1l
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @miika3
#Vip MaZeN تم التعديل بواسطة 🎸 ⋅    
