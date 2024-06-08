from aiogram import Dispatcher

from src.middlewares.data_middleware import SessionDataMiddleware
from src.middlewares.db_session import DatabaseMiddleware


def register_global_middlewares(dp: Dispatcher, session) -> None:
    dp.update.middleware(DatabaseMiddleware(session))

    dp.message.middleware(SessionDataMiddleware())
    dp.callback_query.middleware(SessionDataMiddleware())