# Обработка запроса на отоборажение имени бегуна

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from db_handler import db_models
from handlers import start


router = Router()


@router.message(Command('name'))
async def cmd_name(message: Message, state: FSMContext):
    # Временная проверка наличия пользователя в базе данных
    user = db_models.get_cup_name_from_person_table(message.from_user.id)
    if user == None:
        await start.cmd_start(message, state)
        return

    cup_name = db_models.get_cup_name_from_person_table(message.from_user.id)
    await message.answer('На твоём стаканчике будет имя ' +
                         str(cup_name) + ' ❤️')
