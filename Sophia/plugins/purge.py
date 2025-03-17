from pyrogram import filters
from Sophia.__main__ import Sophia
from Sophia import HANDLER
import asyncio
from pyrogram.enums import ChatType

@Sophia.on_message(filters.command("purge", prefixes=HANDLER) & filters.me)
async def purge_messages(_, message):
  if message.chat.type == ChatType.PRIVATE:
    return await message.reply("This command only works in groups!")
  if not message.reply_to_message:
    return await message.reply("Reply to the message you want to delete from.")
  start = message.reply_to_message.id
  end = message.id
  for x in range(start, end_msg_id + 1, 100):
    try:
      x = list(range(x+1, x+101))
      await Sophia.delete_messages(message.chat.id, x)
      await asyncio.sleep(1.2)
    except Exception as e:
      logging.error(f"Error deleting message {x}: {str(e)}")
  await message.reply("Purge complete.")