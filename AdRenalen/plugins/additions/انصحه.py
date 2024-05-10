import asyncio
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from AdRenalen import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.enums import ParseMode, ChatMemberStatus




@app.on_message(command(['انصحه']))
def call_random_member(client:Client, message:Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    if chat_id in iddof:
        return
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nاوعي تكسر حد حبك بجد ❤",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nالسكوت يدل علي القوه وليث الضعف 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nتجاهل الناس وحقق حلمك لان الناس مش هتنفعك 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nكما تدين تدان فا لا تاذي الاخرين 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nأنت مسؤول عما تشعر به، لكنك لست مسؤولاً عما يشعرون به 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nلا تترك صلاتك مهما كان وذكر ربك طول الاوقات 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nالفائزون لا يخبرون أسرار تدريبهم نحو الأهداف الكبيرة 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nبلاش تتعلق بلناس الحوليك لان كلهم اوقات وهيمشو 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nعندما تتغير الرياح يجب علينا تعديل اتجاه البحر بدلا من الشراع 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nالحياة مثل الأمواج، عليك فقط أن تجد توازنك لعدم الغرق 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nالنظر ف عيون الشخاص عند مخاطبتهم 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\n لو تعطي الثقه بي اي شخص 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nناتوانیت تاریکی لەبیربکەیت پێویستە مۆمێك دروست بکەیت🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nاترك الاشياء التي تئذيك دائما 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nالأمور لا تتحدد بمرور موقف ما، بل بالاستجابات لذلك الموقف 🖤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nصلي علي النبي ❤•",
         f"-النصيحه دي ليك♥•\n│ ل {random_member_mention}\nاعتني بسمعتك جيدا فستثبت للك الايام انها اغلي ما تملك"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
@app.on_message(command(['نداء','ن']))
def call_random_member(client:Client, message:Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    if chat_id in iddof:
         return
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"أنت أجمل منا{random_member_mention}🌚🖤•",
        f"جمالك لا يوصف{random_member_mention}⚡♥•",
        f"الحب في قلب الجميع{random_member_mention}🍭💞•",
        f"ماتيجي تتكلم معانو ياعم ولا مكسوف{random_member_mention}😂♥•",
        f"لقد اندهشت المدينة من جمالك{random_member_mention}🙊🥰•",
        f"ماتيجي خاص ونجيب اشخاص{random_member_mention}😂🤭•",
        f"طظ فيك{random_member_mention}😔😂•",
         f"بحبك بس هحبك اكتر لو اتكلمت{random_member_mention}😂💘•",
         f"ماتراعي يا لبن المراعي{random_member_mention}🥰😂😂•",
         f"ما تصلي علي النبي كده {random_member_mention}✨❤•"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
