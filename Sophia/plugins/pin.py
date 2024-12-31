from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("pin", prefixes=HANDLER) & filters.user(OWN))
async def pin_message(_, message):
    if message.reply_to_message:
        try:
            await Sophia.pin_chat_message(message.chat.id, message.reply_to_message_id, both_sides=True)
            await message.delete()
        except Exception as e:
            if str(e) == """Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "messages.UpdatePinnedMessage")""":
                await message.reply("❌ You need admin access to do this!")
            elif str(e).startswith("""Telegram says: [420 FLOOD_WAIT_X] - A wait of"""):
                sec = int(e.split()[8])
                await asyncio.sleep(sec)
                await Sophia.pin_chat_message(message.chat.id, message.reply_to_message_id)
            else:
                await message.reply(f"**Error:** `{e}`")
    else:
        await message.reply("ℹ️ Please reply to a message to unpin")


@Sophia.on_message(filters.command("unpin", prefixes=HANDLER) & filters.user(OWN))
async def unpin_message(_, message):
    if message.reply_to_message:
        try:
            await Sophia.unpin_chat_message(message.chat.id, message.reply_to_message_id)
        except Exception as e:
            if str(e) == """Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "messages.UpdatePinnedMessage")""":
                await message.reply("❌ You need admin access to do this!")
            elif str(e).startswith("""Telegram says: [420 FLOOD_WAIT_X] - A wait of"""):
                sec = int(e.split()[8])
                await asyncio.sleep(sec)
                await Sophia.unpin_chat_message(message.chat.id, message.reply_to_message_id)
            else:
                await message.reply(f"**Error:** `{e}`")
    else:
        await message.reply("ℹ️ Please reply to a message to unpin")
        

MOD_NAME = 'Pin'
MOD_HELP = ".pin (reply) - To pin the replied message!\n.unpin (reply) - To unpin the replied message!"
