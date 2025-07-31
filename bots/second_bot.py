from aiogram import Bot
from aiogram.types import Message
from aiogram import html
from mystates_sec import ArizaState,AdmingaMurojaatState
from aiogram.fsm.context import FSMContext
from keyboards import start_button,admin_murojaat_tasdiq

async def bot_ishga_tushganda(bot:Bot):
    await bot.send_message(5312290570, "Bot ishga tushdi...")

async def bot_toxtaganda(bot:Bot):
    await bot.send_message(5312290570, "Bot ishdan to'xtadi...")


async def start_bosganda(message:Message):
    await message.answer(f"Assalomu alaykum {html.bold(message.from_user.full_name)}\nQuydagi mrnyulardan birini tanlang", reply_markup=start_button)

async def arizani_bosganda(message: Message, state:FSMContext):
    await message.answer("Ariza topshirshga hush kelibsiz\n Ism familiyangizni kiriting")
    await state.set_state(ArizaState.ism_familiya)

async def ariza_ism_familiya(message:Message, state:FSMContext):
    await state.update_data(ism_familiya=message.text)
    await message.answer("Ism familiyangzi qabul qilindi. \nYoshingizni kiriting")
    await state.set_state(ArizaState.yosh)

async def ariza_yosh(message:Message, state:FSMContext):
    await state.update_data(yosh=message.text)
    await message.answer("Yoshingiz qabul qilindi. \nQaysi texnlogiyalarni bilasiz?")
    await state.set_state(ArizaState.texnologiya)

async def ariza_texnologiya(message:Message, state:FSMContext):
    await state.update_data(texnologiya=message.text)
    await message.answer("Texnik bilimlaringiz qabul qilindi. \nTelefon raqamingizni kiryting")
    await state.set_state(ArizaState.tel_raqam)

async def ariza_tel_raqam(message:Message, state:FSMContext):
    await state.update_data(tel_raqam=message.text)
    await message.answer("Telefon raqamingiz qabul qilindi. \nManzilingizni kiriting!")
    await state.set_state(ArizaState.manzil)

async def ariza_manzil(message:Message, state:FSMContext):
    await state.update_data(manzil=message.text)
    await message.answer("Manzilingiz qabul qilindi. \nQanchaga ishlamoqchisiz kiriting!")
    await state.set_state(ArizaState.narx)

async def ariza_narx(message:Message, state:FSMContext):
    await state.update_data(narx=message.text)
    await message.answer("Fikringiz qabul qilindi. \nTalabami yoki ishchi?")
    await state.set_state(ArizaState.kasb)

async def ariza_kasb(message:Message, state:FSMContext):
    await state.update_data(kasb=message.text)
    await message.answer("Fikringiz qabul qilindi. \nMurojat vaqtini kiriting??")
    await state.set_state(ArizaState.mur_vaqt)

async def ariza_mur_vaqt(message:Message, state:FSMContext):
    await state.update_data(mur_vaqt=message.text)
    await message.answer("Fikringiz qabul qilindi. \nMaqsadingiz nima?")
    await state.set_state(ArizaState.maqsad)

async def ariza_maqsad(message:Message, state:FSMContext):
    await state.update_data(maqsad=message.text)
    malumotlar = await state.get_data()
    elon = f"""
Ish joyi kerak:

👨‍💼 Xodim: {malumotlar['ism_familiya']}
🕑 Yosh: {malumotlar['yosh']}
📚 Texnologiya: {malumotlar['texnologiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {malumotlar['tel_raqam']}
🌐 Hudud: {malumotlar['manzil']}
💰 Narxi: {malumotlar['narx']}
👨🏻‍💻 Kasbi: {malumotlar['kasb']}
🕰 Murojaat qilish vaqti: {malumotlar['mur_vaqt']} 
🔎 Maqsad: {malumotlar['maqsad']}

#xodim #python    
    """
    await message.answer(f"Maqsadingiz qabul qilindi. \n--------------------------------------{elon}\nArizani tasdiqlaysizmi?")
    await state.set_state(ArizaState.tasdiq)

async def ariza_tasdiq(message:Message, state:FSMContext, bot: Bot):
    await state.update_data(tasdiq=message.text)
    if message.text.lower()=='ha':
        await message.answer("Arizangiz qabul qilindi. Tasdiqdan o'tsa 24-48 soat oralig'ida e'loningiz kanalga tashlanadi.")
        malumotlar = await state.get_data()
        elon = f"""
        Sizga {message.from_user.mention_html(message.from_user.first_name)} dan yangi ariza keldi
Ish joyi kerak:
    
👨‍💼 Xodim: {malumotlar['ism_familiya']}
🕑 Yosh: {malumotlar['yosh']}
📚 Texnologiya: {malumotlar['texnologiya']}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {malumotlar['tel_raqam']}
🌐 Hudud: {malumotlar['manzil']}
💰 Narxi: {malumotlar['narx']}
👨🏻‍💻 Kasbi: {malumotlar['kasb']}
🕰 Murojaat qilish vaqti: {malumotlar['mur_vaqt']} 
🔎 Maqsad: {malumotlar['maqsad']}
    
#xodim #python    
    """
        await bot.send_message(5312290570, elon)
    else:
        await message.answer("Arizangiz qabul qilinmadi!")
async def stop_bosganda(message: Message, state: FSMContext):
    mystate = await state.get_state()
    if mystate==None:
        await message.answer("Siz shundog'am ariza yubormayabsiz!")
    else:
        await message.answer("Ariza topshirish bekor qilindi!")
        await state.clear()



async def help_bosganda(message:Message):
    matn=f"""
/start - botni ishga tushiradi
/ariza - Ariza yozadi
/stop - ariza yozishni bekor qiladi

Hamda yuqoridagi knopkalar orqali boshqa amallar bajarsangiz bo'ladi!
"""
    await message.answer(matn)

async def admina_murojaat_function(message:Message,state:FSMContext):
    await message.answer("Adminga yubormoqchi bo'lgan fikringizni bildiring!")
    await state.set_state(AdmingaMurojaatState.matn)

async def admin_m_matn(message:Message,state:FSMContext):
    await state.update_data(matn=message.text)
    await message.answer("Shu matnni yuborishga ishonchingiz komilmi?", reply_markup=admin_murojaat_tasdiq)


async def admin_m_tasdiq(message:Message,state:FSMContext, bot:Bot):
    malumotlar=await state.get_data()
    if message.text == 'ha':
        await bot.send_message(5312290570, text=f"{message.from_user.mention_html(message.from_user.first_name)}")