from aiogram import Bot,types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message,CallbackQuery
from core.keyboards.inline import *
from core.keyboards.reply import *
from core.message.opport_text import *
from core.google_sheet.sheet import *




async def how_get_there(message:Message,state:FSMContext):
    await message.answer(text_how_get_there())

async def our_partners(message:Message):
    await message.answer(text_our_partner())

async def download(message:Message):
    await message.answer(text_download())







