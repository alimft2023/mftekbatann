import asyncio
import datetime

async def myFunc(x):   # coroutine
    await asyncio.sleep(5)
    return x

print(datetime.datetime.now())
print(asyncio.run(myFunc(100)))
print(asyncio.run(myFunc(200)))
print(datetime.datetime.now())