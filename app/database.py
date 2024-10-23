from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker    

DB_HOST = 'localhost'
DB_PORT =5432
DB_USER ='postgres'
DB_PASS ='root'
DB_NAME = 'postgres'


DATABASE_URL=f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


engine = create_async_engine(DATABASE_URL)

async_session_marker= sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)

class Base(DeclarativeBase):
    pass
