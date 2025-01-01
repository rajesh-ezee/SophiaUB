from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os
from pyrogram.enums import ChatMemberStatus

@Sophia.on_message(filters.command("pin", prefixes=HANDLER) & filters.user(OWN))
async def pin_message(_, message):
    if message.reply_to_message:
        try:
            a = await Sophia.get_chat_member(message.chat.id, message.from_user.id)
            if a.status == ChatMemberStatus.MEMBER or not a.privileges.can_pin_messages:
                return await message.reply("**You don't have enough admin rights to use this command ❌**")
            await Sophia.pin_chat_message(message.chat.id, message.reply_to_message_id, both_sides=True)
            await message.delete()
        except Exception as e:
            if str(e).startswith("""Telegram says: [420 FLOOD_WAIT_X] - A wait of"""):
                sec = int(str(e).split()[8])
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
            a = await Sophia.get_chat_member(message.chat.id, message.from_user.id)
            if a.status == ChatMemberStatus.MEMBER or not a.privileges.can_pin_messages:
                return await message.reply("**You don't have enough admin rights to use this command ❌**")
            await Sophia.unpin_chat_message(message.chat.id, message.reply_to_message_id)
            await message.delete()
        except Exception as e:
            if str(e).startswith("""Telegram says: [420 FLOOD_WAIT_X] - A wait of"""):
                sec = int(str(e).split()[8])
                await asyncio.sleep(sec)
                await Sophia.unpin_chat_message(message.chat.id, message.reply_to_message_id)
            else:
                await message.reply(f"**Error:** `{e}`")
    else:
        await message.reply("ℹ️ Please reply to a message to unpin")
        

MOD_NAME = 'Pin'
MOD_HELP = ".pin (reply) - To pin the replied message!\n.unpin (reply) - To unpin the replied message!"
