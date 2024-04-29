import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AdRenalen import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AdRenalen import app
from asyncio import gather
from pyrogram.errors import FloodWait


@app.msg_text in ["المالك", "مالك"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        allAdminsss = bot.get_chat_administrators(chat_id)
        Admins = [Admin.user for Admin in allAdminsss if Admin.status == "creator"]
        for user in Admins:
            user_inf = bot.get_chat(user.id)

            Photo_user = f"https://t.me/{user_inf.username}"
            ttxtx = f"""- معلومات المالك : 
✯︙name: ⤿ {user_inf.first_name}

✯︙user : ⤿  @{user_inf.username}

✯︙Bio: ⤿ #{user_inf.bio}"""

        try:
            bot.send_photo(
                chat_id,
                Photo_user,
                caption=ttxtx,
                reply_to_message_id=message.id,
                reply_markup=Get_prerson(name=user_inf.first_name, id=user_inf.id),
            )

        except:
            bot.send_message(
                chat_id,
                ttxtx,
                reply_to_message_id=message.id,
                reply_markup=Get_prerson(name=user_inf.first_name, id=user_inf.id),
            )
                    
