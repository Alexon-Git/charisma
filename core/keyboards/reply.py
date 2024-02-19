from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить номер телефона",request_contact=True)
        ]
    ],
    resize_keyboard=True,
)


application_button = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Возможности"),
                    KeyboardButton(text="Спикеры"),
                ],
                [
                    KeyboardButton(text="Расписание"),
                    KeyboardButton(text="Тарифы"),
                ]
            ],
            resize_keyboard=True,
        )


back_but = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Вернуться в главное меню")
                ]
            ],
            resize_keyboard=True,    
        )

