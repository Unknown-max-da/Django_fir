from aiogram import Bot
from aiogram.types import Message
from aiogram import html

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

async def start_bosganda(message: Message):
    ism = message.from_user.first_name
    familiya = message.from_user.last_name
    username = message.from_user.username
    chat_id = message.chat.id
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO bot_user(ism,familiya,username,chat_id) values(%s, %s, %s, %s)
    """, (ism,familiya,username,chat_id))
    await message.answer(f"Assalomu alaykum {html.bold(message.from_user.full_name)}")


async def bot_ishga_tushganda(bot: Bot):
    await bot.send_message(5312290570, "Bot ishga tushdi...")

async def bot_toxtaganda(bot: Bot):
    await bot.send_message(5312290570, "Bot to'xtadi...")

async def all_users(message: Message):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("select * from bot_user")
    userlar=cur.fetchall()
    chiqar=[]
    print("USERLAR RO'YHATI\n\n")
    for user2 in userlar:
        chiqar += f"{user2[0]}){user2[2]} | {user2[3]} | @{user2[1]} | {user2[4]}\n"
    await message.answer(chiqar, reply_to_message_id=message.message_id)