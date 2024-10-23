# from pydantic import model_validator, root_validator
# from pydantic_settings import BaseSettings
# class Settings(BaseSettings):
#     DB_HOST : str
#     DB_PORT : int
#     DB_USER : str
#     DB_PASS : str
#     DB_NAME : str

#     @root_validator(skip_on_failure=True)
#     def get_database_url(cls,v):
#         v["DATABASE_URL"]=f'postgresql+asyncpg://{v['DB_USER']}:{v['DB_PASS']}@{v['DB_HOST']}:{v['DB_PORT']}/{v['DB_NAME']}'
#         return v
#     class Config:
#         env_file='.env'

# settings=Settings()

# print(settings.DB_HOST)
# print(settings.DATABASE_URL)
