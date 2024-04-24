from pyrogram import enums
from pyrogram import types
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AdRenalen import app

hmses = {}

@app.on_message(filters.reply & filters.regex("همسه") & filters.group)
async def reply_with_link(client, message):
    user_id = message.reply_to_message.from_user.id
    my_id = message.from_user.id
    bar_id = message.chat.id
    start_link = f"https://t.me/{(await app.get_me()).username}?start=hms{my_id}to{user_id}in{bar_id}"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("‹ اضغط لارسال الهمسة 💘 ›", url=start_link)]
        ]
    )
    await message.reply_text("‹ اضغط لارسال الهمسة 💘 ›", reply_markup=reply_markup)

waiting_for_hms = False
@app.on_message(filters.command("start"), group=89)
async def hms_start(client, message):
    if message.text.split(" ", 1)[-1].startswith("hms"):
        global waiting_for_hms, hms_ids
        hms_ids = message.text
        waiting_for_hms = True
        await message.reply_text(
            "- ارسل الهمسه الان💘 ⋅",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("‹ الغاء الهمسه 💘 ›", callback_data="hms_cancel")]]
            ),
        )

@app.on_message(filters.private & filters.text & ~filters.command("start"), group=88)
async def send_hms(client, message):
    global waiting_for_hms
    if waiting_for_hms:
        to_id = int(hms_ids.split("to")[-1].split("in")[0])
        from_id = int(hms_ids.split("hms")[-1].split("to")[0])
        in_id = int(hms_ids.split("in")[-1])
        to_url = f"tg://openmessage?user_id={to_id}"
        from_url = f"tg://openmessage?user_id={from_id}"
        
        hmses[str(to_id)] = {"hms": message.text, "bar": in_id}
        
        await message.reply_text("- تم ارسال الهمسة 💘 ⋅")
        
        await app.send_message(
    chat_id=in_id,
    text=f"-᚜ - الـ مستخدم » ⦗ [{(await app.get_chat(to_id)).first_name}](tg://openmessage?user_id={to_id}) ⦘ 💘 ⋅\n-᚜ - لديك همسة من الـ مستخدم » ⦗ [{(await app.get_chat(from_id)).first_name}](tg://openmessage?user_id={from_id}) ⦘ 💘 ⋅\n -᚜ - لا يمكن لاحد غيرك رؤية الهمسة 💘 ⋅",
    reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton("‹ اظغط لرؤية الهمسه 💘 ›", callback_data="hms_answer"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐎𝑳𝐈𝐕𝐄𝐀 ›", url=f"http://t.me/SOURCEOliVEA"),
            ]
        ]                   

         ),parse_mode=enums.ParseMode.MARKDOWN)
        
        waiting_for_hms = False
     
@app.on_callback_query(filters.regex("hms_answer"))
async def display_hms(client, callback):
    print("Inside display_hms function")
    in_id = callback.message.chat.id
    who_id = callback.from_user.id
    
    if hmses.get(str(who_id)) is not None:
        if hmses.get(str(who_id))["bar"] == in_id:
            await callback.answer(hmses.get(str(who_id))["hms"], show_alert=True)
    else:
        await callback.answer("عيل خبيث داخل تشوف الـ همسه لي 😂💘 ⋅", show_alert=True)
        
@app.on_callback_query(filters.regex("hms_cancel"))
async def cancel_hms(client, callback):
    print("Inside cancel_hms function")
    global waiting_for_hms
    waiting_for_hms = False
    
    await client.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        text="- تم الغاء الهمسه 💘 ⋅",)


from googletrans import Translator

translator = Translator()

async def english(message):
    translation = translator.translate(message, src='ar', dest='en')
    return translation.text

async def arabic(message):
    translation = translator.translate(message, src='en', dest='ar')
    return translation.text

@app.on_message(filters.command("ترجم", ""), group=158802982)
async def targma(client, message):
    replied_message = message.reply_to_message
    if replied_message:
        replied_text = replied_message.text
        if replied_text:
            if replied_text.isascii(): 
                translated_text = await arabic(replied_text)
            else:
                translated_text = await english(replied_text)            
            await asyncio.sleep(1) 
            await message.reply(translated_text)
        else:
            await message.reply("الرسالة التي تم الرد عليها لا تحتوي على نص.")
    else:
        await message.reply("الرجاء الرد على الرسالة لترجمتها.")
