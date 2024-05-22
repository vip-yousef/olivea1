from pyrogram.types import InlineKeyboardButton

import config
from AdRenalen import app


def start_panel(_):
    buttons = [
        [InlineKeyboardButton(text="الاوامر ⚙", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="🔺️ - مطور السورس - 🔻", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="✅ - قناه السورس - ✅", url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [InlineKeyboardButton(text="الاوامر ⚙", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="🔺️ - مطور السورس - 🔻", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="✅ - قناه السورس - ✅", url=config.SUPPORT_CHANNEL),
        ],
    [
            InlineKeyboardButton(
                text="اضف البوت الي مجموعتك ✅ ⋅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],]
    return buttons
