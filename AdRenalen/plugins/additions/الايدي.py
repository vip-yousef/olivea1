import asyncio
from asyncio import gather
from pyrogram import Client, filters
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
import time
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
    bio = user.bio
    chat = message.chat.title
    chat_id = message.chat.id
   
    photo = user.photo.big_file_id
    if photo:
        photo = await client.download_media(photo)
    else:
        photo = None
    
    if user.id not in id:
        id[user.id] = []
    
    idd = len(id[user.id])
    
    caption = f"name : {first_name}\nid : {user_id}\nuser : [@{username}]\nbio : {bio}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")]])
    
    await message.reply_photo(photo=photo, caption=caption, reply_markup=reply_markup)

@app.on_callback_query(filters.regex("heart"))
async def heart(client, query: CallbackQuery):
    callback_data = query.data.strip()
    callback_request = callback_data.replace("heart", "")
    user_id = int(callback_request)
    user = await client.get_chat(user_id)
    
    if user.id not in id:
        id[user.id] = []
    
    if query.from_user.mention not in id[user.id]:
        id[user.id].append(query.from_user.mention)
    else:
        id[user.id].remove(query.from_user.mention)
    
    idd = len(id[user.id])
    
    caption = f"⌯ 𝐍𝐚𝐦𝐞 :{message.from_user.mention}\n⌯ 𝐔𝐬𝐞𝐫 :@{message.from_user.username}\n⌯ 𝐈𝐝 :`{message.from_user.id}`\n⌯ 𝐁𝐢𝐨 :{usr.bio}\n⌯ 𝐂𝐡𝐚𝐭 : {message.chat.title}\n⌯ 𝐈𝐝 𝐜𝐡𝐚𝐭:`{message.chat.id}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")]])
    
    await query.edit_message_text(caption, reply_markup=reply_markup)

iddof = []
@app.on_message(
    command(["قفل جمالي","تعطيل جمالي"])
    & filters.group
)
async def lllock(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if message.chat.id in iddof:
        return await message.reply_text("جمالي معطل من قبل√")
      iddof.append(message.chat.id)
      return await message.reply_text(" تم تعطيل جمالي بنجاح√")
   else:
      return await message.reply_text("لازم تكون ادمن\n√")

@app.on_message(
    command(["فتح جمالي","تفعيل جمالي"])
    & filters.group
)
async def idljjopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if not message.chat.id in iddof:
        return await message.reply_text("جمالي مفعل من قبل√")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح جمالي بنجاح √")
   else:
      return await message.reply_text("هذا الامر للأدمن فقط")



@app.on_message(filters.command(['تفعيل التعديل'], prefixes=""))
async def iddlock(client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if message.chat.id in italy:
            return await message.reply_text("تم تفعيل التعديل \n√")
        italy.append(message.chat.id)
        return await message.reply_text("تم تفعيل التعديل بنجاح \n√")
    else:
        return await message.reply_text("يجب عليك أن تكون مشرف اولا \n√")

@app.on_message(filters.command(['تعطيل التعديل'], prefixes=""))
async def iddopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if not message.chat.id in italy:
        return await message.reply_text("التعديل معطل من قبل \n√")
      italy.remove(message.chat.id)
      return await message.reply_text("تم فتح تعطيل بنجاح \n√")
   else:
      return await message.reply_text("لازم تكون ادمن اولا \n√")



@app.on_message(
    command(["جمالي"])
    & filters.group
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا مز انت \n※ \n🐉: {ik} %😂❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )

    
