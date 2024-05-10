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

The_Stayle = [ "وربنا جامد يعم رقمك زيرو كام  😂♥️ ،","علفكرا صورتي احسن منك 😂♥️ ،","الجمال عدا الخيال 😂♥️ ،","متراعي ي لبن المراعي 😂♥️ ،","مش ناوي تغير الصوره دي بقا 😂♥️ ،","غيرها بقا لما بشوفها بتخض 😂♥️ ،"]
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

@app.on_message(filters.command(["ا"], ""))
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
    
    caption = f" {choice(The_Stayle)} \n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 : {first_name}\n🎃 ¦𝙸𝙳 : {user_id}\n🎯 ¦𝚄𝚂𝙴𝚁 : [@{username}]\n💌 ¦𝙱𝙸𝙾 : {bio}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} ❤️", callback_data=f"heart{user_id}")]])
    
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
    
    caption = f" {choice(The_Stayle)} \n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 : {first_name}\n🎃 ¦𝙸𝙳 : {user_id}\n🎯 ¦𝚄𝚂𝙴𝚁 : [@{username}]\n💌 ¦𝙱𝙸𝙾 : {bioo}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} ❤️", callback_data=f"heart{user_id}")]])
    
    await query.edit_message_text(caption, reply_markup=reply_markup)
