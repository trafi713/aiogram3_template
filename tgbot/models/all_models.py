from sqlalchemy import Column, BigInteger, String

from tgbot.settings.database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
