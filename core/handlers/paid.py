from aiogram import Bot,types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message,CallbackQuery
from core.keyboards.inline import *
from core.keyboards.reply import *
from core.message.opport_text import *
from core.google_sheet.sheet import *
from core.sending.in_group import sending_question

group = "-4129579886"

class SP(StatesGroup):
    choice = State()
    # question = State()


async def how_get_there(message:Message,state:FSMContext):
    await message.answer(text_how_get_there())

async def our_partners(message:Message):
    await message.answer(text_our_partner())

async def download(message:Message):
    await message.answer(text_download())

async def question_spiker(message:Message, state:FSMContext):
    await message.answer("Выберите спикера:",reply_markup=speaker_but())

async def choose_question(call:CallbackQuery, state:FSMContext):
    await call.answer()
    await state.set_state(SP.choice)
    name = call.data
    name = name.split("_")[1]
    await state.update_data(name = name)
    print(name)
    await call.message.edit_text("Напишите Ваш вопрос")


async def sending_question(message:Message, bot:Bot, state:FSMContext ):
    # await call.answer()
    global  qroup
    data = await state.get_data()
    name_sp = data.get('name')
    mess = message.text
    qroup = "-4129579886"
    question = f"Задал вопрос: [{message.from_user.first_name}] (tg://user?id={message.from_user.id})\n\nСпикер: *{name_sp}*\n\nВопрос:\n{mess}"
    await state.clear()
    try:
        await bot.send_message("-4138167534", question, parse_mode='markdown')
        await message.answer('Спасибо за вапрос, он направлен спикеру.')
    except Exception as ex:
        await message.answer("Произошла ошибка отправки сообщения. Подойдите к администратору.")
        if str(ex) == "TelegramBadRequest: Telegram server says - Bad Request: user not found":
            print(f"User not found")
        else:
            print(f"Неизвестная ошибка:\nex = {ex}")

    # sending_question(message.from_user.id, message.from_user.first_name, name, mess)