from dataclasses import dataclass

from environs import Env



@dataclass
class TgConfig:
    token: str


@dataclass
class DbConfig:
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


@dataclass
class Config:
    tg: TgConfig
    db: DbConfig


def load_config() -> Config:
    env = Env()
    env.read_env()

    return Config(
        tg=TgConfig(
            token=env.str("BOT_TOKEN"),
        ),
        db=DbConfig(
            database=env.str("DB_NAME"),
            user=env.str("DB_USER"),
            password=env.str("DB_PASS"),
            host=env.str("DB_HOST"),
            port=env.int("DB_PORT"),
        )
    )
