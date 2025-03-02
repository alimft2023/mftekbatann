import asyncio
import datetime

async def myFunc(x):   # coroutine
    await asyncio.sleep(5)
    print(x)

async def main():
    a = asyncio.create_task(myFunc(100))
    b = asyncio.create_task(myFunc(200))

    await a
    await b

print(datetime.datetime.now())
asyncio.run(main())
print(datetime.datetime.now())