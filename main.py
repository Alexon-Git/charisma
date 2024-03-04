import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from core.settings import settings
from core.handlers.basic import *
from core.handlers.application import *
from core.handlers.paid import *

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()

    dp.message.register(start_command, Command(commands=['start']))
    dp.callback_query.register(reg_phone, F.data.startswith("political"))
    # dp.callback_query.register(reg_name, F.data.startswith("political"))
    # dp.message.register(reg_phone, LK.name)
    # dp.message.register(check_CRM, LK.phone)
    dp.message.register(greeting_application, LK.phone) #Главное меню
    dp.callback_query.register(opport_tab,F.data.startswith("opport_"))
    dp.callback_query.register(opport_tab_two,F.data.startswith("opporttab_"))
    dp.callback_query.register(skip_speaker,F.data.startswith("count_"))

    dp.message.register(Opportunities,lambda message: message.text == "Возможности")
    dp.message.register(main_menu, lambda message: message.text == "Вернуться в главное меню")
    dp.message.register(Speaker,lambda message: message.text == "Спикеры")
    dp.message.register(check,lambda message: message.text == "Уже оплатил")
    dp.message.register(tariff,lambda message: message.text == "Тарифы")


    dp.message.register(timetable,lambda message: message.text == "Расписание")


    dp.message.register(how_get_there,lambda message: message.text == "Как проехать")
    # dp.message.register(chek,lambda message: message.text == "Нетворкинг чат")
    # dp.message.register(chek,lambda message: message.text == "Задать вопрос спикеру")
    dp.message.register(our_partners,lambda message: message.text == "Наши партнеры")
    dp.message.register(download,lambda message: message.text == "Скачать стикер-пак")

    

    # dp.message.register()


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

    # запуск машины .\.venv\Scripts\activate 