from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.settings import worksheet_no_pay
from aiogram.utils.keyboard import InlineKeyboardBuilder

soglasie = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Даю согласие", callback_data="political")],
])


def opport_but(): # собирает кнопки из гугл таблицы
    but =  InlineKeyboardBuilder()
    s = worksheet_no_pay.col_values(2)[2:]
    for i in range(len(s)):
        but.button(text=s[i],callback_data=f"opport_{i+3}") # указывается строчка на котрочкой расположена кнопка
    but.adjust(1)
    return but.as_markup()

def opport_tab_but(but_text,strok): # собирает кнопки 2 уровня из гугл таблицы
    but =  InlineKeyboardBuilder()
    # but_text = worksheet_no_pay.cell(strok,4).value #сначала строка потом столбец
    but.button(text=but_text,callback_data=f"opporttab_{strok}") # указывается строчка на котрочкой расположена кнопка
    # but.button(text="Вернуться в главн меню",callback_data=f"Back") # указывается строчка на котрочкой расположена кнопка
    but.adjust(1)
    return but.as_markup()


def but_pay(but_text):
    but = InlineKeyboardBuilder()
    but.button(text= but_text, callback_data="pay")
    but.adjust(1)
    return but.as_markup()


def but_speakers(sheet,s):
    but = InlineKeyboardBuilder()
    v = int(len(sheet))-1
    strel_L = "◀️"
    strel_R = "▶️"
    crest = "✖"
    call_L = "count_-1"
    call_R = "count_+1"
    if int(s) == 1:
        strel_L = crest
        call_L = "__"
    if int(s) == (int(len(sheet))-1):
        strel_R = crest
        call_R = "__"
    but.button(text=strel_L, callback_data=call_L)
    but.button(text= f"{s}/{v}", callback_data="__")
    but.button(text=strel_R, callback_data=call_R)
    but.adjust(3)
    return but.as_markup()





find_partner_but = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Я в деле!", callback_data="in_business")],
])
find_partner_business_but = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Оплатить тариф", callback_data="pay_find_partner")],
])

partner_offers_but = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Стать партнером", callback_data="become_partner")],
])

stocks_but = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить билет", callback_data="buy_ticket")],
])


