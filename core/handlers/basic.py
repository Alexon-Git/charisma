from aiogram import Bot,types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message,CallbackQuery
from core.keyboards.inline import *
from core.keyboards.reply import *
from core.message.text import *
from core.message.opport_text import *
from core.settings import worksheet_paid
from core.google_sheet.sheet import text_paid
from core.google_sheet.user_verification import check_user
from core.filter.veref import Checking_phone
# from core.settings import cursor, connection   # переменная подключения к базе
# import database


# async def start_command(message: Message): # привет
#     builder = create_start_buttons()
#     await message.answer("Приветственное сообщение", reply_markup=builder.as_markup())
#     if not(await database.check_user(user_id = message.from_user.id)):
#         await database.set_new_user(user_id= message.from_user.id,username= message.from_user.first_name)


async def main_menu(message:Message,state:FSMContext):
    #сделать проверку оплативших
    await state.clear()
    await message.answer(application_text_google, reply_markup=application_button, parse_mode="html")


class LK(StatesGroup):
    name = State()
    phone = State()
    size = State()

async def start_command(message: Message):
    await message.answer(start_text, reply_markup=soglasie,)

async def reg_name(call: CallbackQuery, state: FSMContext):
    await state.set_state(LK.name)
    await call.answer()
    await call.message.answer("Как я могу к Вам обращаться?")

#сохзранение в базу id и указанное имя
async def reg_phone(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(LK.phone)
    await call.message.answer( f"Приятно прознакомиться {call.from_user.first_name}. Напишите или отправте свой номер телефона, чтобы я нашел Вас в базе", reply_markup=phone,  parse_mode="html")


# происходить проверка по CRM
    
# async def handlers_LI(message:Message, bot:Bot, state: FSMContext):
#     if Checking_phone(message.text):
#         await state.clear()
#         # await state.get_state(Opport.opport_menu)
#         await state.clear()
#         await message.answer(application_text_google, reply_markup=application_button, parse_mode="html")
#     else:
#         info = await state.get_data()
#         FIO = info.get('FIO')
#         if message.text == None:
#             phone = message.contact.phone_number
#         else:
#              phone = message.text
#         # UserRegistration(FIO, message.from_user.first_name, phone, message.from_user.id, message.chat.id)
#         await message.answer('Вы успешно зарегистрировались, теперь вы можете отвечать и отправлять заявки',reply_markup=but_catalog)
#         await state.clear()







async def check_CRM(message: Message, state: FSMContext):

    if message.text == None:
        phone = message.contact.phone_number
    else:
        phone = message.text

    if len(phone)< 10:
        return await message.answer("Вы ввели не корректный номер, повторите попытку.")
    

    if check_user(phone[-10:]):
        await state.clear()
        await message.answer(f"{text_paid()}", reply_markup=paid_button, parse_mode="html")
    else:
        await state.clear()
            # await state.get_state(Opport.opport_menu)
        
        await message.answer(f"{application_text_google}", reply_markup=application_button, parse_mode="html")
   






    # print(message.contact.phone_number)
    # if 'NoneType' == message.contact.phone_number:
    #     print("yes")
    #     await message.answer('Отправьте номер через кнопку')
    # else:
    # # print(message)
    #     phone = message.contact.phone_number
    #     print('no')
    #     print(phone[-10:])
    #     if check_user(phone[-10:]):
    #         text = text_paid()
    #         await message.answer(text, reply_markup=paid_button, parse_mode="html")
    #     else:
    #         await state.clear()
    #     # await state.get_state(Opport.opport_menu)
    #         await message.answer(application_text_google, reply_markup=application_button, parse_mode="html")
   


async def greeting_application(message: Message, state: FSMContext):
    await state.clear()
    # await state.get_state(Opport.opport_menu)
    await message.answer(application_text_google, reply_markup=application_button)


async def check(message: Message, state: FSMContext):
    # https://t.me/idenphonesBot?start=8899
    text = text_paid()
    await message.answer(text, reply_markup=paid_button)






