from aiogram import Bot,types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message,CallbackQuery
from core.keyboards.inline import *
from core.keyboards.reply import *
from core.message.text import *
from core.settings import cursor, connection   # переменная подключения к базе
# import database


# async def start_command(message: Message): # привет
#     builder = create_start_buttons()
#     await message.answer("Приветственное сообщение", reply_markup=builder.as_markup())
#     if not(await database.check_user(user_id = message.from_user.id)):
#         await database.set_new_user(user_id= message.from_user.id,username= message.from_user.first_name)


class LK(StatesGroup):
    name = State()
    phone = State()
    size = State()

async def start_command(message: Message):
    await message.text(start_text, reply_markup=coglasie)

async def reg_name(call: CallbackQuery, state: FSMContext):
    await state.set_state(LK.name)
    await call.answer()
    await call.message.text("Как я могу к Вам обращаться?")

#сохзранение в базу id и указанное имя
async def reg_phone(message: Message, state: FSMContext):
    await state.set_state(LK.phone)
    await message.answer( f"Приятно прознакомиться {message.from_user.first_name}. Напишите свой номер телефона, чтобы я нашел Вас в базе", reply_markup=phone)


# происходить проверка по CRM
async def check_CRM(message: Message, state: FSMContext):
    await message.text()