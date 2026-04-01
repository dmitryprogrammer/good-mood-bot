from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
import os
import logging
import asyncio

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.info)

bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher()

@dispatcher(commands=['start'])
async def start_message(message: types.Message):
    await message.reply("Привет! Я бот хорошего настроения!")

async def main():
    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
