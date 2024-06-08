from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import User


class Repo:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_user(self, user_id: int) -> User:
        stmt = select(User).where(User.id == user_id)
        result = await self.session.scalar(stmt)
        return result
