from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src import Config, load_config


def get_async_session():
    config: Config = load_config()
    engine = create_async_engine(config.db.connection_url())
    async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
    return async_session_maker
