import random 
from pyrogram import filters,Client,enums
from AdRenalen import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import ChatPermissions
from strings.filters import command
from AdRenalen.mongo.nightmodedb import nightdb,nightmode_on,nightmode_off,get_nightchats 



CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages = False,
    can_send_other_messages = False,
    can_send_polls = False,
    can_change_info = False,
    can_add_web_page_previews = False,
    can_pin_messages = False,
    can_invite_users = False )


OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages = True,
    can_send_other_messages = True,
    can_send_polls = True,
    can_change_info = True,
    can_add_web_page_previews = True,
    can_pin_messages = True,
    can_invite_users = True )
    
buttons = InlineKeyboardMarkup([[InlineKeyboardButton("๏ تمكين ๏", callback_data="add_night"),InlineKeyboardButton("๏ تعطيل ๏", callback_data="rm_night")]])         

@app.on_message(filters.command("nightmode") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg", caption="✧¦انقر على أحد الأزرار لتمكين وتعطيل أمر الوضع الليلي لإغلاق وفتح المجموعات تلقائي•",reply_markup=buttons)
              
     
@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query : CallbackQuery):
    data = query.data 
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id" : chat_id})
    administrators = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)     
    if user_id in administrators:   
        if data == "add_night":
            if check_night:        
                await query.message.edit_caption("✧¦الوضع الليلي ممكن بالفعل !")
            elif not check_night :
                await nightmode_on(chat_id)
                await query.message.edit_caption("✧¦تمت إضافة الوضع الليلي في هذه المجموعة إلى Data Twenty، Clock Group 𝟏𝟐يغلق في الليل وفي 𝟖 وسوف تفتح في الصباح") 
        if data == "rm_night":
            if check_night:  
                await nightmode_off(chat_id)      
                await query.message.edit_caption("✧¦تم حذف معلومات الحالة الليلية من قاعدة البيانات")
            elif not check_night:
                await query.message.edit_caption("✧¦الوضع الليلي معطل بالفعل!") 
            
    
    
async def start_nightmode() :
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for add_chat in chats:
        try:
            await app.send_video(
                add_chat,
                video="https://telegra.ph/file/76986c01e5b54f7b7c503.mp4",
                caption= f"سيتم إغلاق المجموعة ئەزیزان🚫🧑🏻‍💻\nأتمنى لك ليلة نوم سعيدة شاد🌚♥️🫶🏻**")
            
            await app.set_chat_permissions(add_chat,CLOSE_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To close Group {add_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Baghdad")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59)
scheduler.start()

async def close_nightmode():
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for rm_chat in chats:
        try:
            await app.send_photo(
                rm_chat,
                photo="https://graph.org/file/765ad5ac25fca83c1d06c.jpg",
                caption= f"**گرووپ کرایەوە ئەزیزان✅🧑🏻‍💻\nبەیانیتان باش🌚♥️🫶🏻**")
            
            await app.set_chat_permissions(rm_chat,OPEN_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To open Group {rm_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Baghdad")
scheduler.add_job(close_nightmode, trigger="cron", hour=8, minute=1)
scheduler.start()

##############################

@app.on_message(command("الوضع اليلي") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg", caption="✧¦انقر فوق أحد الأزرار لتمكين الوضع الليلي وتعطيله.",reply_markup=buttons)

