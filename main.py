from dotenv import load_dotenv
from os import getenv
import asyncio

load_dotenv()

async def num():
    async def time():
        print("Один")
        await asyncio.sleep(1)
        print("Два")
    
    for i in range(7):
        await time()

async def main():
    await asyncio.gather(num())

asyncio.run(main())
