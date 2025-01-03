from pyrogram import *
from Sophia import *
import asyncio 
from Sophia.helpers.cloner_communication import *

def ohk():
    loop = asyncio.get_event_loop()
    if loop.is_running():
        asyncio.ensure_future(wait_for_stop_signal())
    else:
        loop.run_until_complete(wait_for_stop_signal())

ohk()
