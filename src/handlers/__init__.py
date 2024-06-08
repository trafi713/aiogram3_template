from aiogram import Dispatcher

from .start import router as start


def register_routes(dp: Dispatcher) -> None:
    dp.include_router(start)
