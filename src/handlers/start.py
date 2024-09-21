from aiogram import types, Router
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import User
from src.filters.is_private import IsChatPrivateFilter

router = Router()
router.message.filter(IsChatPrivateFilter())

@router.message(CommandStart())
async def start_handler(message: types.Message,
                        session: AsyncSession,
                        user: User) -> None:
    user_id: int = message.from_user.id
    full_name: str = message.from_user.full_name
    username: str | None = message.from_user.username

    if not user:
        user = User(
            id=user_id,
            full_name=full_name,
            username=username
        )

        session.add(user)

    if not user.is_active:
        user.is_active = True

    if user.full_name != full_name:
        user.full_name = full_name

    if user.username != username:
        user.username = username

    await session.commit()

    await message.answer(f"Hello {user.full_name}")
