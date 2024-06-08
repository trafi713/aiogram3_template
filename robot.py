import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from aiogram.fsm.storage.memory import MemoryStorage

from src import load_config
from src.handlers import register_routes
from src.middlewares import register_global_middlewares
from src.settings.db_setup import get_async_session

logger = logging.getLogger(__name__)


async def main() -> None:
    config = load_config()
    storage = MemoryStorage()

    bot = Bot(token=config.tg.token, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    ))

    dp = Dispatcher(storage=storage)

    session_pool = get_async_session()

    # Register middlewares
    register_global_middlewares(dp, session_pool)

    # Register routes
    register_routes(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await storage.close()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped by user")
