from pathlib import Path

from environs import Env
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class TgConfig(BaseModel):
    token: str


class DbConfig(BaseModel):
    database: str
    user: str
    password: str
    host: str
    port: int

    def connection_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:"
            f"{self.port}/{self.database}"
        )


class RedisConfig(BaseModel):
    host: str
    port: int
    db: int


class Settings(BaseSettings):
    tg: TgConfig
    db: DbConfig
    redis: RedisConfig


def load_settings() -> Settings:
    env = Env()
    env.read_env()

    return Settings(
        tg=TgConfig(
            token=env.str("BOT_TOKEN"),
        ),
        db=DbConfig(
            database=env.str("DB_NAME"),
            user=env.str("DB_USER"),
            password=env.str("DB_PASS"),
            host=env.str("DB_HOST"),
            port=env.int("DB_PORT"),
        ),
        redis=RedisConfig(
            host=env.str("REDIS_HOST"),
            port=env.int("REDIS_PORT"),
            db=env.int("REDIS_DB"),
        )
    )


settings = load_settings()
