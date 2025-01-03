from Sophia import *
from pyrogram import *
import asyncio
import aiofiles
from variables import *

# This function used for stop ub using SophiaCloner signel
async def wait_for_stop_signal():
  while not DEVELOPER_MODE:
    try: 
      async with aiofiles.open('communication.txt', 'r') as f:
        c = await f.read()
        if 'stop' in c:
          await Sophia.send_message('me', "Stop signel received killing process..")
          logging.warn("Stop signel received killing process..")
          await Sophia.stop()
          exit()
        await asyncio.sleep(10)
    except FileNotFoundError:
      logging.info("Looks like userbot not deployed using SophiaCloner bot")
      break
    
