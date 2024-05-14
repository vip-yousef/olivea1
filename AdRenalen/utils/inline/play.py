import math
from AdRenalen import app 
from pyrogram.types import InlineKeyboardButton
from AdRenalen.utils.formatters import time_to_seconds

def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    [
            InlineKeyboardButton(text="𖣂.𝙴𝙽𝙳", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝙿𝙰𝚄𝚂𝙴", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="𝚁𝙴𝚂𝚄𝙼𝙴.𖣂", callback_data=f"ADMIN Replay|{chat_id}"),
        ],[
            InlineKeyboardButton(text="𖣂.𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ", url=f"https://t.me/SOURCEOLIVEA"),
            InlineKeyboardButton(text="𝙶𝚁𝙾𝚄𝙿.𖣂", url=f"https://t.me/D1_FD"),
        ],[
            InlineKeyboardButton(text="𓄼⦁ 𝗠ٰٖ𝗮ٰٖ𝗭ٰٖ𝗲ٰٖ𝗡ٰٖ ➪🇳🇱⦁𓄹", url=f"https://t.me/WA_AdRenalen"),
        ],[
            InlineKeyboardButton(text="اضف البوت الي جروبك او قناتك ⚡", url=f"https://t.me/{app.username}?startgroup=true")]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="𖣂.𝙴𝙽𝙳", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝙿𝙰𝚄𝚂𝙴", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="𝚁𝙴𝚂𝚄𝙼𝙴.𖣂", callback_data=f"ADMIN Replay|{chat_id}"),
        ],[
            InlineKeyboardButton(text="𖣂.𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ", url=f"https://t.me/SOURCEOLIVEA"),
            InlineKeyboardButton(text="𝙶𝚁𝙾𝚄𝙿.𖣂", url=f"https://t.me/D1_FD"),
        ],[
            InlineKeyboardButton(text="𓄼⦁ 𝗠ٰٖ𝗮ٰٖ𝗭ٰٖ𝗲ٰٖ𝗡ٰٖ ➪🇳🇱⦁𓄹", url=f"https://t.me/WA_AdRenalen"),
        ],[
            InlineKeyboardButton(text="اضف البوت الي جروبك او قناتك ⚡", url=f"https://t.me/{app.username}?startgroup=true")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"ModyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"ModyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="Resume",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
