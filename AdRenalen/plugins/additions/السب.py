import random
from config import *
from AdRenalen import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatMemberStatus


def Who(m, user_id):
  user = m.chat.get_member(user_id)
  if user.status == ChatMemberStatus.OWNER:
    return "المالك"
  elif user.status == ChatMemberStatus.ADMINISTRATOR:
    return "مشرف"
  elif user.status == ChatMemberStatus.MEMBER:
    return "العضو"

forward = []
cursing = []
#####==> By JABWA <==#####
@app.on_message(filters.command("تف", "") & filters.group & filters.reply)
def jabwa(c, m):
  ID_BOT = app.id
  first_name = m.reply_to_message.from_user.first_name
  id = m.reply_to_message.from_user.id
  if id == OWNER_ID:
    return m.reply("• لا يمكنك التف علي المطور ❤️✌️")
  if id == ID_BOT:
    return m.reply("• عاوزني اتف علي نفسي يعبيط 😂")
  if id == DEVELOPERS:
    return m.reply("• لا يمكنك التف علي مطورين السورس 🧑‍✈️")
  Text =f"""
• تم التف علي هذا الشخص

※ المتفوف علي {first_name}

 اععع اي القرف ده 🤢
"""
  JABWA = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  m.reply_animation("https://t.me/DEVSOLiVEA/13",caption=Text,reply_markup=JABWA)

@app.on_message(filters.command("تخ", "") & filters.group & filters.reply)
def jabwa(c, m):
  ID_BOT = app.id
  first_name = m.reply_to_message.from_user.first_name
  id = m.reply_to_message.from_user.id
  if id == OWNER_ID:
    return m.reply("• لا يمكنك قتل المطور ❤️✌️")
  if id == ID_BOT:
    return m.reply("• عاوزني اقتل نفسي 😂")
  if id == DEVELOPERS:
    return m.reply("• لا يمكنك قتل مطورين السورس 🧑‍✈️")
  Text =f"""
• تم قتل هذا الشخص

※ المقتول {first_name}

 ان لله وان اليه راجعون ⚰😭
"""
  JABWA = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  m.reply_animation("https://t.me/DEVSOLiVEA/14",caption=Text,reply_markup=JABWA)
  
