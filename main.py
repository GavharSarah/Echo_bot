from aiogram import Bot, Dispatcher, types
from asyncio import run
db=Dispatcher()


async def echo(message:types.Message,bot:Bot):
    await message.copy_to(chat_id=message.chat.id)


async def start():
    db.message.register(echo)
    bot=Bot(token="7832835307:AAFk8WjtezHe6TzMPdgJg6Q9UMVx957sQ8A")
    await db.start_polling(bot,polling_timeout=0.5)

run(start())