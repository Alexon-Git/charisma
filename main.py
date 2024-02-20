import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from core.settings import settings
from core.handlers.basic import *
from core.handlers.application import *

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()

    dp.message.register(start_command, Command(commands=['start']))
    dp.callback_query.register(reg_name, F.data.startswith("political"))
    dp.message.register(reg_phone, LK.name)
    # dp.message.register(check_CRM, LK.phone)
    dp.message.register(greeting_application, LK.phone)
    dp.message.register(Opportunities,lambda message: message.text == "Возможности")
    dp.callback_query.register(opport_tab,F.data.startswith("opport_"))
    dp.callback_query.register(opport_tab_two,F.data.startswith("opporttab_"))

    # dp.message.register(back_callback, lambda message: message.text == "Вернуться в главное меню")
    # сделать проверку по пользователям и возвращать на кнопки возможности, спикеры....
    

    # dp.message.register()


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

    # запуск машины .\.venv\Scripts\activate 