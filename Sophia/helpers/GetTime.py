import asyncio

async def GetTime(txt, wait=False):
  units = {'h': 3600000, 'm': 60000, 's': 1000, 'd': 86400000}
  if not isinstance(txt, str) or len(txt) < 2 or not txt[:-1].isdigit() or txt[-1] not in units:
    raise TypeError("Invalid time format")
  ms = int(txt[:-1]) * units[txt[-1]]
  if wait:
    return await asyncio.sleep(ms / 1000)
  return ms