from pydantic import model_validator, root_validator
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    # DB_HOST : str
    # DB_PORT : int
    # DB_USER : str
    # DB_PASS : str
    # DB_NAME : str

    # @root_validator(skip_on_failure=True)
    # def get_database_url(cls,v):
    #     v["DATABASE_URL"]=f'postgresql+asyncpg://{v['DB_USER']}:{v['DB_PASS']}@{v['DB_HOST']}:{v['DB_PORT']}/{v['DB_NAME']}'
    #     return v
    # class Config:
    #     env_file='.env'
    SECRET_KEY:str
    ALGORITHM: str

    SECRET_KEY='A/AhRtJ1jOwO45NjI4fAnHqrNb3+pCpDp1FrEtjzAIY='
    ALGORITHM='HS256'

settings=Settings()

