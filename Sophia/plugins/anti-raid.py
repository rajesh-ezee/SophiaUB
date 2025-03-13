"""from Sophia import *
from pyrogram import *
from pyrogram.types import *

raids = {}

@Sophia.on_message(filters.command('antiraid') & filters.me & filters.group):
async def raid_setting(_, m):
  global raids
  if m.chat.id in raids:
    del raids[m.chat.id]
    return await m.reply("done")
  raids[m.chat.id] = True
  return await m.reply("done")

@Sophia.on
"""