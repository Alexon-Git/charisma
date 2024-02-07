from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone = ReplyKeyboardMarkup(reply_keyboard=[
    [KeyboardButton(text="Поделиться номером", request_contart=True)],
])