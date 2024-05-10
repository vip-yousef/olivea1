from pyrogram import Client, filters
from pyrogram.types import Message
from AdRenalen import app 

@app.on_message(filters.command(["واتس"], ""), group=26577)
async def check_whatsapp(client, message):
    split_text = message.text.split(' ')
    if len(split_text) > 1:
        phone_number = split_text[1]
        try:
            parsed_number = parse(phone_number, None)
            if is_possible_number(parsed_number):
                await message.reply(f"رقم الهاتف {phone_number} به واتساب.")
            else:
                await message.reply(f"رقم الهاتف {phone_number} لا يوجد عليه واتساب.")
        except Exception as e:
            await message.reply("تم تقديم رقم هاتف غير صالح")
    else:
        await message.reply("يرجى تقديم رقم الهاتف بعد الأمر \nهكذا واتس +2010128345678")
