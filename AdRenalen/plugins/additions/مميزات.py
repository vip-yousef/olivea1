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
mute = []
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

※ بواسطة {first_name}

 اععع اي القرف ده 🤢
"""
  JABWA = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  m.reply_animation("https://t.me/DEVSOLiVEA/14",caption=Text,reply_markup=JABWA)

@app.on_message(filters.command("تخ", "") & filters.group & filters.reply)
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
• تم قتل هذا الشخص

※ بواسطة {first_name}

 ان لله وان اليه راجعون ⚰😭
"""
  JABWA = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  m.reply_animation("https://t.me/DEVSOLiVEA/14",caption=Text,reply_markup=JABWA)

@app.on_message(filters.command("كشف", "") & filters.group)
def jabwa(c, m):
  name = m.reply_to_message.from_user.first_name
  id = m.reply_to_message.from_user.id
  user = m.reply_to_message.from_user.username
  rank = f"{Who(m,m.reply_to_message.from_user.id)}"
  money = random.randint(1, 100)
  Text =f"""**
• الاسم : {name}
• الايدي : {id}
• اليوزر : {user}
• الرتبه {rank}
• سعر الكشف : {money} جنيه 😂❤️
**"""
  return m.reply(Text)

@app.on_message(filters.command("قفل الدردشه", "") & filters.group)
def of_chat(c, m):
  idchat = m.chat.id
  mention = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_ID:
    return m.reply("يجب انت تكون ادمن للقيام بذلك")
  c.set_chat_permissions(idchat, ChatPermissions())
  m.reply(f"• تم قفل الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("فتح الدردشه", "") & filters.group)
def on_chat(c, m):
  idchat = m.chat.id
  mention = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_ID:
    return m.reply("يجب انت تكون ادمن للقيام بذلك")
  c.set_chat_permissions(idchat, ChatPermissions(can_send_messages=True, can_send_media_messages=True))
  m.reply(f"• تم فتح الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("قفل السب بالكتم", "") & filters.group)
def of_cursing(c, m):
  idchat = m.chat.id
  name = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_BOT:
    return m.reply("يجب انت تكون ادمن للقيام بذلك")
  cursing.append(idchat)
  m.reply(f"• تم قفل السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح السب بالكتم", "") & filters.group)
def on_cursing(c, m):
  idchat = m.chat.id
  name = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_BOT:
    return m.reply("يجب انت تكون ادمن للقيام بذلك")
  cursing.remove(idchat)
  m.reply(f"• تم فتح السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("قفل التوجيه بالكتم", "") & filters.group)
def of_forward(c, m):
  idchat = m.chat.id
  name = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_BOT:
    return m.reply("يجب انت تكون ادمن للقيام بذلك")
  forward.append(idchat)
  m.reply(f"• تم قفل التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح التوجيه بالكتم", "") & filters.group)
def on_forward(c, m):
  idchat = m.chat.id
  name = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_ID:
    return m.reply("يجب انت تكون ادمن للقيام بذلك")
  forward.remove(idchat)
  m.reply(f"• تم فتح التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("مسح المكتومين", "") & filters.group)
def remove(c, m):
  idchat = m.chat.id
  name = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_BOT:
    return m.reply("يجب انت تكون ادمن للقيام بذلك")
  for member in c.get_chat_members(idchat):
    if member.user.is_bot == True:
      pass
    elif member.user.is_deleted == True:
      pass
    else:
      mute.remove(member.user.id)
  m.reply(f"• تم مسح المكتومين\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.text & filters.group)
def msg(c, m):
  text = m.text
  idchat = m.chat.id

  if m.from_user.id in mute:
    m.delete()

  insults = ["كس","كسمك","كسختك","عير","كسخالتك","خرا بالله","عير بالله","كسخواتكم","كحاب","مناويج","مناويج","كحبه","ابن الكحبه","فرخ","فروخ","طيزك","طيزختك","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","ابن العرص","منايك","متناك","احا","ابن المتناكه","زبك","عرص","زبي","خول","لبوه","لباوي","ابن اللبوه","منيوك","كسمكك","متناكه","احو","احي","يا عرص","يا خول","قحبه","القحبه","شراميط","العلق","العلوق","العلقه","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","االمنيوك","كسمككك","الشرموطه","ابن العرث","ابن الحيضانه","زبك","خول","زبي","قاحب","تيزك"]
  if str(text) in insults:
    if idchat in cursing:
      a = c.get_chat_member(idchat, m.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not m.from_user.id == OWNER_BOT:
         m.delete()
         mute.append(m.from_user.id)
         Text =f"""
♪ عذرا {m.from_user.mention} ⚡ .
♪ ممنوع الشتائم ⚡ .
"""
         m.reply(Text,quote=True)

  if m.forward_date:
    if idchat in forward:
      a = c.get_chat_member(idchat, m.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not m.from_user.id == OWNER_BOT:
         m.delete()
         mute.append(m.from_user.id)
         Text =f"""
♪ عذرا {m.from_user.mention} ⚡ .
♪ ممنوع التوجيه هنا ⚡ .
"""
         m.reply(Text,quote=True)
