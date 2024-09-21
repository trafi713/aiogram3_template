from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession

from src import settings


class DatabaseHelper:
    def __init__(self,
                 url: str,
                 echo: bool = False,
                 echo_pool: bool = False,
                 pool_size: int = 10,
                 max_overflow: int = 10) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False
        )

    async def dispose(self) -> None:
        await self.engine.dispose()


db_helper = DatabaseHelper(
    url=settings.db.connection_url()
)
