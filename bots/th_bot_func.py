from aiogram import Bot
from aiogram.types import Message
from aiogram import html
from aiogram.fsm.context import FSMContext

async def bot_ishga_tushganda(bot:Bot):
    await bot.send_message(5312290570, "Bot ishga tushdi...")

async def bot_toxtaganda(bot:Bot):
    await bot.send_message(5312290570, "Bot ishdan to'xtadi...")

async def start_bosganda(message:Message):
    await message.answer(f"Assalomu alaykum {html.bold(message.from_user.full_name)}")

async def stop_bosganda(message: Message, state: FSMContext):
    mystate = await state.get_state()
    if mystate==None:
        await message.answer("Siz shundog'am ariza yubormayabsiz!")
    else:
        await message.answer("Ariza topshirish bekor qilindi!")
        await state.clear()