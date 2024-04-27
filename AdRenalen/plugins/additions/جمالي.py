from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import requests
from AdRenalen import app 

SUPPORT_CHAT = "MGIMT"

@app.on_message(filters.command(["wish","حەز","هیوا","خۆزگە"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def wish(_, m):
    if len(m.command) < 2:
        await m.reply("اكتب رغباتك أو تفضيلاتك مع الامر")
        return 

    api = requests.get("https://nekos.best/api/v2/happy").json()
    url = api["results"][0]['url']
    text = m.text.split(None, 1)[1]
    wish_count = random.randint(1, 100)
    wish = f"**🍓 اسمك {m.from_user.first_name}!**\n"
    wish += f"**🍓 رغبتك: {text} **\n\n"
    wish += f"**🍓 نسبه حدوثها: {wish_count}% **"
    
    await app.send_animation(
        chat_id=m.chat.id,
        animation=url,
        caption=wish,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("تحديثات اوليفيا", url=f"https://t.me/{SUPPORT_CHAT}")]])
    )
            
    
BUTTON = [[InlineKeyboardButton("تحديثات اوليفيا", url=f"https://t.me/{SUPPORT_CHAT}")]]
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"

@app.on_message(filters.command(["cute","کیوت","كیوت","جمالي","قشتی"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def cute(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_name)})"
    mm = random.randint(1, 100)
    CUTE = f"**🍓 {mention}\nنسبه جمالك يقلبي {mm}% 🥺🫶🏻**"

    await app.send_document(
        chat_id=message.chat.id,
        document=CUTIE,
        caption=CUTE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )
    
help_text = """
» ᴡʜᴀᴛ ɪꜱ ᴛʜɪꜱ (ᴡɪꜱʜ):
ʏᴏᴜ ʜᴀᴠɪɴɢ ᴀɴʏ ᴋɪɴᴅ ᴏꜰ 
(ᴡɪꜱʜᴇꜱ) ʏᴏᴜ ᴄᴀɴ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ᴛᴏ ʜᴏᴡ ᴘᴏꜱꜱɪʙʟᴇ ᴛᴏ ʏᴏᴜʀ ᴡɪꜱʜ!
ᴇxᴀᴍᴘʟᴇ:» /wish : ɪ ᴡᴀɴᴛ ᴄʟᴀꜱꜱ ᴛᴏᴘᴘᴇʀ 
» /wish : ɪ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ɪᴘʜᴏɴᴇ 
» /cute : ʜᴏᴡ ᴍᴜᴄʜ ɪ ᴀᴍ ᴄᴜᴛᴇ 
"""
