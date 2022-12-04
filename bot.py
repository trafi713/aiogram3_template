import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from tgbot import load_config
from tgbot.handlers.echo import echo_router
from tgbot.handlers.user.user_handlers import user_router
from tgbot.middlewares import DbMiddleware
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.settings.database.setup import create_db_session

logger = logging.getLogger(__name__)


def register_global_middleware(dp: Dispatcher, config, session_pool):
    dp.message.outer_middleware(ConfigMiddleware(config))
    dp.callback_query.outer_middleware(ConfigMiddleware(config))
    dp.message.outer_middleware(DbMiddleware(session_pool))
    dp.callback_query.outer_middleware(DbMiddleware(session_pool))


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Bot started')

    config = load_config('.env')
    storage = MemoryStorage()

    bot = Bot(token=config.tg.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)
    session_pool = await create_db_session(config)

    register_global_middleware(dp, config, session_pool)

    for router in [
        user_router,
        echo_router,
    ]:
        dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped')
