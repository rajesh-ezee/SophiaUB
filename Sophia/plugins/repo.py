from Sophia import *
from pyrogram import *

@Sophia.on_message(filters.command("repo", prefixes=HANDLER) & filters.user('me'))
async def repo(_, message):
  if message.reply_to_message:
    return await message.reply_to_message.reply("https://t.me/rajeshrakis | https://t.me/Ghostt_Batt", disable_web_page_preview=True)
  await message.reply("https://t.me/rajeshrakis | https://t.me/Ghostt_Batt", disable_web_page_preview=True)
