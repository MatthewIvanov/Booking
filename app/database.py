from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

DB_HOST = 'localhost'
DB_PORT =5432
DB_USER ='postgres'
DB_PASS ='root'
DB_NAME = 'postgres'


TEST_DB_HOST = 'localhost'
TEST_DB_PORT =5432
TEST_DB_USER ='postgres'
TEST_DB_PASS ='root'
TEST_DB_NAME = 'test_booking_db'



if settings.MODE=='TEST':
    DATABASE_URL=f'postgresql+asyncpg://{TEST_DB_USER}:{TEST_DB_PASS}@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}'
    DATABASE_PARAMS={'poolclass': NullPool}
else:
    DATABASE_URL=f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    DATABASE_PARAMS={}






engine = create_async_engine(DATABASE_URL,**DATABASE_PARAMS)

async_session_maker= sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)

class Base(DeclarativeBase):
    pass
