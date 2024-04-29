import os
import time
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from strings.filters import command
from AdRenalen import app
from pyrogram.enums import ChatMemberStatus

@app.on_message(~filters.private & command(["المالك","المنشئ"]), group=2)
async def instatus(app, message):
  async for owner in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
    if owner.status == enums.ChatMemberStatus.OWNER:
      saidi = app.get_users(owner.user.id)
      bio = app.get_chat(owner.user.id).bio
      JABWA = InlineKeyboardMarkup([[InlineKeyboardButton(saidi.first_name, url=f"https://t.me/{saidi.username}")]])
      async for x in c.get_chat_photos(saidi.id, limit=1):
        photo = x.file_id
      await m.message(photo,caption=f"**• name : [{saidi.first_name}](tg://user?id={saidi.id})\n• user : [@{saidi.username}]\n• id : {saidi.id}\n• bio : {bio}**",reply_markup=JABWA,quote=True)
