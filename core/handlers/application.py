from aiogram import Bot,types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message,CallbackQuery
from core.keyboards.inline import *
from core.keyboards.reply import *
from core.message.opport_text import *
from core.google_sheet.sheet import all_sheet_no_pay

class Opport(StatesGroup):
    opport_menu = State()
    tab_one = State()
    tab_two = State()


async def back_callback(call: CallbackQuery, state: FSMContext,bot:Bot): # функция возвращения назад
    state_name = await state.get_state()
    print(state_name)
    if state_name == Opport.tab_one.state :
        print("провалился в меню возможности")
        await state.set_state(Opport.opport_menu)
        await call.message.answer("Что интересно узнать?", reply_markup=opport_but())
        # await call.message.answer("Выберите модель:", reply_markup=model(price(brand),1))
    elif state_name == Opport.tab_two.state :
        await state.set_state(Opport.tab_one)
        s = (call.data).split('_')
        strok = s[1]
        text = worksheet_no_pay.cell(strok,3).value
        print(text)
        await call.message.edit_text(text, reply_markup=opport_tab_but(strok))

        





async def Opportunities(message: Message, state:FSMContext): # Обработчик кнопки возможности
    await state.set_state(Opport.opport_menu)
    await message.answer("Что интересно узнать?", reply_markup=opport_but())
    list = all_sheet_no_pay()
    await state.update_data(sheet_no_pay = list) # достается весь лист и хранится в памяти машинного состояния


async def opport_tab(call:CallbackQuery, state:FSMContext): # Проваливается на 2 уровень
    await state.set_state(Opport.tab_one)
    s = (call.data).split('_')
    strok = int(s[1])
    sheet_state = await state.get_data()
    sheet = sheet_state.get("sheet_no_pay")
    text = sheet[strok-1][2]
    but_tab = sheet[strok-1][3]
    if (but_tab == None) or but_tab == "":
        await call.message.edit_text(text)
    else:
        await call.message.edit_text(text, reply_markup=opport_tab_but(but_tab,strok))


async def opport_tab_two(call:CallbackQuery, state:FSMContext): # Проваливается на 3 уровень
    await state.set_state(Opport.tab_two)
    s = (call.data).split('_')
    strok = int(s[1])
    sheet_state = await state.get_data()
    sheet = sheet_state.get("sheet_no_pay")
    text = sheet[strok-1][4]
    but_tab = sheet[strok-1][5]
    if (but_tab == None) or but_tab == "":
        await call.message.edit_text(text)
    else:
        await call.message.edit_text(text, reply_markup=but_pay(but_tab))



