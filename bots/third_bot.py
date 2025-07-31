import asyncio
from aiogram import Dispatcher,Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart,Command
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
import th_bot_func

TOKEN = "8478774727:AAHJhDjUz7PxHpaiyEOADsEJCKLsdaTRztU"
dp=Dispatcher()

async def main():
    dp.startup.register(th_bot_func.bot_ishga_tushganda)
    dp.message.register(th_bot_func.start_bosganda, CommandStart())
    dp.message.register(th_bot_func.stop_bosganda, Command('stop'))

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.shutdown.register(th_bot_func.bot_toxtaganda)

    await bot.set_my_commands([
        BotCommand(command='/start', description="Botni ishga tushirish..."),
        BotCommand(command="/stop", description="Botni tohtatadi...")
    ])
    await dp.start_polling(bot)

asyncio.run(main())