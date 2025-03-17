from Restart import restart_program
from Sophia import *
from Sophia.helpers import *
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os
  
@Sophia.on_message(filters.command(["restart", 'trestart'], prefixes=HANDLER) & filters.user(OWN))
async def restart(_, message):
  if message.command[0] == 'trestart':
    try:
      txt = " ".join(message.command[1:])
      if int(txt[:-1]) <= 5 and txt.endswith('s'):
        return await message.reply("Time should be greater than 5 sec.")
      x = await GetTime(txt)
      await message.edit(f"Done! userbot will be restarted in {txt}")
      await asyncio.sleep(x)
    except: return await message.edit("Nooo, this is not correct time format.\nUse: `.trestart 1h`")
  await message.edit("Restarting...")
  restart_program()
