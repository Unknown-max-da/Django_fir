import asyncio
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from new_bot_func import bot_ishga_tushganda, bot_toxtaganda, start_bosganda, all_users
from aiogram.filters import CommandStart, Command
from aiogram.types import BotCommand

import psycopg2
def get_connection():
    database_rtx = psycopg2.connect(
        dbname = 'telegram_db',
        user = 'postgres',
        password = 'N17122010el',
        host = 'localhost',
        port = '5432'

    )
    return database_rtx

TOKEN='8024076542:AAGy8Urc0h5wN-7LGTEuxYncURLxQyd6xhI'
dp = Dispatcher()

async def main():
    dp.startup.register(bot_ishga_tushganda)
    dp.message.register(start_bosganda, CommandStart())
    dp.message.register(all_users, Command('users'))
    bot = Bot(token = TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.shutdown.register(bot_toxtaganda)
    await bot.set_my_commands([
        BotCommand(command='/users', description="Hamma userlarni ko'rsatadi...")
    ])
    await dp.start_polling(bot)

asyncio.run(main())
