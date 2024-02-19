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

def opport_tab_but(strok): # собирает кнопки 2 уровня из гугл таблицы
    but =  InlineKeyboardBuilder()
    but_text = worksheet_no_pay.cell(strok,4).value #сначала строка потом столбец
    but.button(text=but_text,callback_data=f"opport_tab_{strok}") # указывается строчка на котрочкой расположена кнопка
    # but.button(text="Вернуться в главн меню",callback_data=f"Back") # указывается строчка на котрочкой расположена кнопка
    but.adjust(1)
    return but.as_markup()




def but_pay(strok):
    but = InlineKeyboardBuilder()
    s = worksheet_no_pay.cell(4,strok)
    but.button(text= s, callback_data="pay")
    but.adjust(1)
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


