from pyrogram import *
from Sophia import *
import asyncio
from ..Database.silent import Silent

silent = Silent()

async def SilentFilter(_, __, m):
  if await silent.get() and m.chat.id not in await silent.get_exceptions():
    try:
      await Sophia.read_chat_history(m.chat.id)
      await Sophia.read_mentions(m.chat.id)
      await Sophia.read_reactions(m.chat.id)
    except: pass

@Sophia.on_message(filters.command('silent') & filters.me)
async def silent(_, m):
  x = await silent.get()
  if x:
    await silent.off()
    return await m.reply("Ilovedher")
  else:
    await silent.on()
    return await m.reply("True")
    
@Sophia.on_message(~filters.me & filters.create(SilentFilter))
@Sophia.on_message_reaction(~filters.me & filters.create(SilentFilter))
async def do_ntg(_, __):
  pass