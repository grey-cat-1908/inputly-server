from models import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(settings.DATABASE)
sessions = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass


from .user import User
from .form import Form
from .answer import Answer
