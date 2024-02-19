from aiogram import Bot,types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message,CallbackQuery
from core.keyboards.inline import *
from core.keyboards.reply import *
from core.message.opport_text import *

class Opport(StatesGroup):
    opport_menu = State()
    tab_one = State()
    tab_two = State()


# async def back_callback(call: CallbackQuery, state: FSMContext,bot:Bot): # функция возвращения назад
#     state_name = await state.get_state()
#     if state_name == Opport.tab_one.state :
#         await state.set_state(Opport.opport_menu)
#         await call.message.answer("Что интересно узнать?", reply_markup=opport_but())
#         # await call.message.answer("Выберите модель:", reply_markup=model(price(brand),1))
#     elif state_name == Opport.tab_two.state :
#         await state.set_state(Opport.tab_one)
#         s = (call.data).split('_')
#         strok = s[1]
#         text = worksheet_no_pay.cell(strok,3).value
#         print(text)
#         await call.message.edit_text(text, reply_markup=opport_tab_but(strok))

        





async def Opportunities(message: Message, state:FSMContext): # Обработчик кнопки возможности
    await state.set_state(Opport.opport_menu)
    await message.answer("Что интересно узнать?", reply_markup=opport_but())


async def opport_tab(call:CallbackQuery, state:FSMContext): # Проваливается на 2 уроветь
    await state.set_state(Opport.tab_one)
    s = (call.data).split('_')
    strok = s[1]
    print(strok)
    text = worksheet_no_pay.cell(strok,3).value
    but_tab = worksheet_no_pay.cell(strok,4).value
    if but_tab == None:
        await call.message.edit_text(text)
    else:
        await call.message.edit_text(text, reply_markup=opport_tab_but(strok))


