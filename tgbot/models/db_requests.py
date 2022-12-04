from sqlalchemy import select, insert

from tgbot.models import *


class DbRequest:
    def __init__(self, session):
        self.session = session

    async def get_user(self, user_id: int):
        sql = select(User).where(User.user_id == user_id)
        request = await self.session.execute(sql)
        return request.scalar()

    async def add_user(self, user_id: int, username: str, full_name: str):
        sql = insert(User).values(user_id=user_id,
                                  username=username,
                                  full_name=full_name).returning('*')
        request = await self.session.execute(sql)
        await self.session.commit()

        return request.first()
