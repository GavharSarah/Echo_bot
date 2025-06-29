from aiogram import Bot, Dispatcher, types
from asyncio import run
from dotenv import load_dotenv
import os


load_dotenv()  # Load variables from .env

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

db=Dispatcher()


async def echo(message:types.Message,bot:Bot):
    await message.copy_to(chat_id=message.chat.id)


async def start():
    db.message.register(echo)
    bot=Bot(token=TOKEN)
    await db.start_polling(bot,polling_timeout=1)

run(start())