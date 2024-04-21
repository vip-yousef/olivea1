#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @SOURCEOliVEA
#𝙳𝙴𝚅 𝙼𝙰𝚉𝙴𝙽 : @ZzZzZl1l
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @miika3
#Vip MaZeN تم التعديل بواسطة 🎸 ⋅

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from AdRenalen import app

@app.on_message(filters.command(["الرابط","/link","لنك","رابط"], "") & filters.group & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("- ارفعني مسول الاول يزميلي 😂💘 ⋅")
    await message.reply_text(f"- تم جلب الرابط بنجاح 😂💘 ⋅\n {invitelink}")
    
#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @SOURCEOliVEA
#𝙳𝙴𝚅 𝙼𝙰𝚉𝙴𝙽 : @ZzZzZl1l
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @miika3
#Vip MaZeN تم التعديل بواسطة 🎸 ⋅