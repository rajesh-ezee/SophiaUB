from pyrogram import *
from Sophia import *
import asyncio
from ..Database.silent import Silent
import logging

silent, info = Silent(), logging.info

async def SilentFilter(_, __, m):
  if await silent.get() and m.chat.id not in await silent.get_exceptions():
    try:
      await Sophia.read_chat_history(m.chat.id)
      await Sophia.read_mentions(m.chat.id)
      await Sophia.read_reactions(m.chat.id)
    except: pass
  return False

@Sophia.on_message(filters.command('silent', prefixes=HANDLER) & filters.me)
async def SetSilent(_, m):
  x = await silent.get()
  if x:
    await silent.off()
    return await m.reply("Successfully, disabled silent mode.")
  await silent.on()
  await m.reply("Success! all your new messages will be marked as read.")
    
@Sophia.on_message(~filters.me & filters.create(SilentFilter))
@Sophia.on_message_reaction(~filters.me & filters.create(SilentFilter))
async def do_ntg(_, __):
  pass