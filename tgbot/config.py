from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class DbConfig:
    user: str
    password: str
    database: str
    host: str
    port: int = 5432


@dataclass
class Config:
    tg: TgBot
    db: DbConfig


def load_config(path: str = '.env'):
    env = Env()
    env.read_env(path)

    return Config(
        tg=TgBot(
            token=env.str('BOT_TOKEN'),
        ),
        db=DbConfig(
            user=env.str('DB_USER'),
            password=env.str('DB_PASS'),
            host=env.str('DB_HOST'),
            port=env.int('DB_PORT'),
            database=env.str('DB_NAME')
        )
    )
