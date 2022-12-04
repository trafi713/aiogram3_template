from aiogram import Router, types

echo_router = Router()


@echo_router.message()
async def echo(message: types.Message):
    await message.answer('⚠️ Неизвестная команда!')
