from aiogram import Router, types
from aiogram.filters import Command

from tgbot.models.db_requests import DbRequest

user_router = Router()


@user_router.message(Command('start'))
async def start(message: types.Message, request: DbRequest):
    user = await request.get_user(message.from_user.id)
    if not user:
        await request.add_user(user_id=message.from_user.id,
                               full_name=message.from_user.full_name,
                               username=message.from_user.username)
    await message.answer(f'Привет {message.from_user.full_name}')
