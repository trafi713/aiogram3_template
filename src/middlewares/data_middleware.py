from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from src.services.repository import Repo


class SessionDataMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        repo: Repo = data.get("repo")

        user = await repo.get_user(event.from_user.id)

        data["user"] = user

        return await handler(event, data)
