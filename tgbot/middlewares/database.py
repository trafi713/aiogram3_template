from typing import Callable, Any, Awaitable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message

from tgbot.models.db_requests import DbRequest


class DbMiddleware(BaseMiddleware):
    def __init__(self, session_pool):
        self.session_pool = session_pool

    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]],
                                         Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]) -> Any:
        async with self.session_pool() as session:
            data['session'] = session
            data['request'] = DbRequest(session)
            result = await handler(event, data)
        return result
