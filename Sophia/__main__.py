import threading
from Sophia import *
from pyrogram import Client, filters
import os
from pyrogram import idle
from subprocess import getoutput as r
from Restart import restart_program
import asyncio 

PWD = f"{os.getcwd()}/"
my_id = None

async def fk():
  await Sophia.start()
  await SophiaBot.start()
  try:
    await SophiaBot.send_photo(
      Sophia.me.id,
      photo="https://i.imgur.com/DuoscLX.jpeg",
      caption=(
        f"**✅ 𝐇𝐞𝐚𝐫𝐭𝐁𝐞𝐚𝐭-✗-𝐁𝐨𝐭\ ⚡**\n\n"
        f"**👾 Version:** {MY_VERSION}\n"
        f"**🥀 Python:** {r('python --version').lower().split('python ')[1]}\n"
        f"**🐬 Owner:** {Sophia.me.first_name if not Sophia.me.last_name else f'{Sophia.me.first_name} {Sophia.me.last_name}'}\n"
        f"**🦋 Join:**@HeartBeat_Muzic"
      )
    )
  except: pass
  await idle()
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(fk())
    
    
