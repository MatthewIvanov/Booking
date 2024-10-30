from datetime import date
from typing import Optional
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.pages.router import router as router_pages
from app.images.router import router as router_images



from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost:6379")
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_pages)
app.include_router(router_images)

origins =[
      '*',
]
app.add_middleware(
      CORSMiddleware,
      allow_origins=origins,
      #allow_creedntails=True,
      allow_methods=['GET','POST','OPTIONS','DELETE','PATCH','PUT'],
      allow_headers=['Coontent-Type','Set-Cookie','Access-Control-Allow-Headers','Access-Authorization'],
)




class HotelSearchArgs:
     def __init__(
               self,
                location:str,
                date_from:date,
                date_to:date,
                has_spa:Optional[bool] = None,
                stars:Optional[int]=Query(None,ge=1,le=5)
            ):
               self.location=location
               self.date_from=date_from
               self.date_to=date_to
               self.has_spa=has_spa
               self.stars=stars

class SHotels(BaseModel):
    address:str
    name:str
    stars:int

@app.get('/hotels')
def get_hotels(
    search_args:HotelSearchArgs=Depends()
    ):
       return search_args



class SBooking(BaseModel):
    room_id:int
    date_from:int
    date_to:int
    
@app.post('/booking')
def add_booking(booking:SBooking):
    pass