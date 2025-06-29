from aiogram import Bot, Dispatcher, types
from asyncio import run
from dotenv import load_dotenv
import os


load_dotenv()  # Load variables from .env

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

db=Dispatcher()

async def startup_answer(bot:Bot):
    await bot.send_message(7499351952, "Bot started successfully!✅")

async def shutdown_answer(bot:Bot):
    await bot.send_message(7499351952, "Bot stopped successfully!❗️ ")


async def echo(message:types.Message,bot:Bot):
    await message.copy_to(chat_id=message.chat.id)


async def start():
    db.startup.register(startup_answer)
    db.message.register(echo)
    db.shutdown.register(shutdown_answer)


    bot=Bot(token=TOKEN)
    await db.start_polling(bot,polling_timeout=1)

run(start())