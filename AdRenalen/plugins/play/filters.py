#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @SOURCEOliVEA
#𝙳𝙴𝚅 𝙼𝙰𝚉𝙴𝙽 : @ZzZzZl1l
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @miika3
#Vip MaZeN تم التعديل بواسطة 🎸 ⋅

from typing import List, Union

from pyrogram import filters


other_filters = filters.group  & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private  & ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, "")
    
#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @SOURCEOliVEA
#𝙳𝙴𝚅 𝙼𝙰𝚉𝙴𝙽 : @ZzZzZl1l
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @miika3
#Vip MaZeN تم التعديل بواسطة 🎸 ⋅