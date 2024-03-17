from aiogram import Bot,types
from aiogram.types import Message

qroup = '-4129579886'

async def sending_question(name_id,name_ques,name_sp,mess, bot:Bot):
    question = f"Задал вопрос: [{name_ques}] (tg://user?id={name_id})\n\nСпикер:*{name_sp}*\n\nВопрос:{mess}"
    global  qroup
    await bot.send_message(qroup, question, parse_mode='markdown')
    return True