import asyncio
from pyrogram import Client, filters ,enums
from strings.filters import command
from pyrogram.types import *
from AdRenalen import app
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ParseMode, ChatMemberStatus

@app.on_message(filters.regex("^المشرفين$"))
async def adlist(_, message):
    chat_id = message.chat.id
    admin = "\n- قائمة المشرفين💘 ⋅\n— — —— — — — ——  — —\n"
    async for admins in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
           admin+=f" -᚜ - اليوزر ⦗ {'@'+admins.user.username if admins.user.username else admins.user.mention} ⦘.الايدي ⦗ {admins.user.id} ⦘\n"
    await message.reply(text=(admin))

@app.on_message(filters.command(["صلاحياتي"], ""))
async def caesarprivileges(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    cae = await client.get_chat_member(chat_id, user_id)
    status = cae.status if cae else None
    if status == ChatMemberStatus.OWNER:
        await message.reply_text("أنت مالك الجروب")
    elif status == ChatMemberStatus.MEMBER:
        await message.reply_text("أنت عضو حقير")
    else:
        privileges = cae.privileges if cae else None 
        can_promote_members = "✅" if (privileges and privileges.can_promote_members) else "❌"
        can_manage_video_chats = "✅" if (privileges and privileges.can_manage_video_chats) else "❌"
        can_pin_messages = "✅" if (privileges and privileges.can_pin_messages) else "❌"
        can_invite_users = "✅" if (privileges and privileges.can_invite_users) else "❌"
        can_restrict_members = "✅" if (privileges and privileges.can_restrict_members) else "❌"
        can_delete_messages = "✅" if (privileges and privileges.can_delete_messages) else "❌"
        can_change_info = "✅" if (privileges and privileges.can_change_info) else "❌"
        hossam = f"صلاحياتك في الجروب:\n\n"
        hossam += f"ترقية الأعضاء: {can_promote_members}\n"
        hossam += f"إدارة الدردشات الصوتية: {can_manage_video_chats}\n"
        hossam += f"تثبيت الرسائل: {can_pin_messages}\n"
        hossam += f"دعوة المستخدمين: {can_invite_users}\n"
        hossam += f"تقييد الأعضاء: {can_restrict_members}\n"
        hossam += f"حذف الرسائل: {can_delete_messages}\n"
        hossam += f"تغيير معلومات الجروب: {can_change_info}\n"
        await message.reply_text(hossam)
