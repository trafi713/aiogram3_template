from aiogram.enums import ChatType
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class IsChatPrivateFilter(BaseFilter):
    async def __call__(self, event: Message | CallbackQuery) -> bool:
        return event.chat.type == ChatType.PRIVATE
