import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from aiogram.fsm.storage.redis import (
    Redis,
    RedisStorage,
    DefaultKeyBuilder
)

from src import settings
from src.database import db_helper
from src.handlers import router as handlers
from src.middlewares import register_global_middlewares

logger = logging.getLogger(__name__)


async def main() -> None:
    storage = RedisStorage(
        Redis(
            host=settings.redis.host,
            port=settings.redis.port,
            db=settings.redis.db,
        ),
        key_builder=DefaultKeyBuilder(with_destiny=True)
    )

    bot = Bot(token=settings.tg.token, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    ))

    dp = Dispatcher(
        storage=storage,
        events_isolation=storage.create_isolation()
    )


    # Register middlewares
    register_global_middlewares(dp)

    # include main router
    dp.include_router(handlers)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await storage.close()
        await db_helper.dispose()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped by user")
