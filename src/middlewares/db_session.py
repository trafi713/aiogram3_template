from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from src.database import db_helper
from src.database.repository import Repo


class DatabaseMiddleware(BaseMiddleware):


    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        async with db_helper.session_factory() as session:
            data['session'] = session
            data['repo'] = Repo(session)

            result = await handler(event, data)
        return result
