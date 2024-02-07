from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.settings import worksheet
from aiogram.utils.keyboard import InlineKeyboardBuilder

coglasie = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Даю согласие", callback_data="political")],
])

