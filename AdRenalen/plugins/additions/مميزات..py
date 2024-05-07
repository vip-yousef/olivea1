import random
from AarohiX import app
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus


def Who(m, user_id):
  user = m.chat.get_member(user_id)
  if user.status == ChatMemberStatus.OWNER:
    return "المالك"
  elif user.status == ChatMemberStatus.ADMINISTRATOR:
    return "مشرف"
  elif user.status == ChatMemberStatus.MEMBER:
    return "العضو"
#####==> By JABWA <==#####
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

