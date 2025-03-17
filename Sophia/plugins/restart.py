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
    try: await GetTime(" ".join(message.command[1:]), True)
    except TypeError: return await message.reply("Nooo, this is not correct time format.\nUse: `.trestart 1h`")
  await message.edit("Restarting...")
  restart_program()
