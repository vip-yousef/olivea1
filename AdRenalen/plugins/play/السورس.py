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



@app.on_message(filters.command(["مازن","زوز"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/477d457991f935bfb233c.jpg",
        caption=f"""• ⌯ Developer Name : ˛ 𝙼𝙰𝚉𝙴𝙽 ⌯ •\n- Devloper Username : @ZzZzZl1l Devloper id : 6816180621 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/SOURCEOliVEA"),
                ],[
                    InlineKeyboardButton(
                        "𓄼⦁ 𝙕ٰٖ𝙤ٰٖ𝙯ٰٖ ➪🇳🇱⦁𓄹", url=f"https://t.me/ZzZzZl1l"), 
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
