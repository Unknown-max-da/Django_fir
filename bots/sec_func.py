import asyncio
from aiogram import Dispatcher,Bot, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart,Command
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
import second_bot
from mystates_sec import ArizaState

TOKEN = "7410948027:AAERAyRXZsVLWzlBGzOubPu2xMmCSr3AKS8"
dp=Dispatcher()

async def main():
    dp.startup.register(second_bot.bot_ishga_tushganda)
    dp.message.register(second_bot.start_bosganda, CommandStart())
    dp.message.register(second_bot.arizani_bosganda, Command('ariza'))
    dp.message.register(second_bot.stop_bosganda, Command('stop'))
    dp.message.register(second_bot.help_bosganda, F.text=='help')
    dp.message.register(second_bot.ariza_ism_familiya, ArizaState.ism_familiya)
    dp.message.register(second_bot.ariza_yosh, ArizaState.yosh)
    dp.message.register(second_bot.ariza_texnologiya, ArizaState.texnologiya)
    dp.message.register(second_bot.ariza_tel_raqam, ArizaState.tel_raqam)
    dp.message.register(second_bot.ariza_manzil, ArizaState.manzil)
    dp.message.register(second_bot.ariza_narx, ArizaState.narx)
    dp.message.register(second_bot.ariza_kasb, ArizaState.kasb)
    dp.message.register(second_bot.ariza_mur_vaqt, ArizaState.mur_vaqt)
    dp.message.register(second_bot.ariza_maqsad, ArizaState.maqsad)
    dp.message.register(second_bot.ariza_tasdiq, ArizaState.tasdiq)
    bot = Bot(token = TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.shutdown.register(second_bot.bot_toxtaganda)

    await bot.set_my_commands([
        BotCommand(command='/start', description="Botni ishga tushirish..."),
        BotCommand(command='/ariza', description="Ariza berish..."),
        BotCommand(command="/stop", description="Botni tohtatadi...")
    ])
    await dp.start_polling(bot)

asyncio.run(main())




















