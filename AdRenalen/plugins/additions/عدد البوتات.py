import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from AdRenalen import app

@app.on_message(filters.command(["طرد البوتات"], "") & filters.group, group=50)
async def ban_bots(client: Client, message: Message):
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and message.from_user.id != 6264438859:
        return
    
    count = 0
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
        if member.user.is_bot:
            try:
                await client.ban_chat_member(message.chat.id, member.user.id)
                count += 1
            except Exception as e:
                print(f"Error banning bot: {e}")
    
    if count > 0:
        await message.reply_text(f"تم طرد {count} بوت بنجاح✅♥")
    else:
        await message.reply_text("لا توجد بوتات لطردها.")

@app.on_message(filters.command(["البوتات"], "") & filters.group, group=5)
async def list_bots(client: Client, message: Message):
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    bot_usernames = []
    count = 0 
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
        if member.user.is_bot:
            bot_usernames.append("@" + member.user.username)
            count += 1

    if count > 0:
        bot_list = "\n".join(bot_usernames)
        await message.reply_text(f"عدد البوتات في المجموعة: {count} \n يوزرات البوتات: {bot_list}")
    else:
        await message.reply_text("لا يوجد بوتات في المجموعة.")
    
