from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import date, time
from typing import Optional
import time

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi import Depends, FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from pydantic import BaseModel
from redis import asyncio as aioredis
from sqladmin import Admin, ModelView

from app.admin.auth import authentication_backend
from app.admin.views import BookingsAdmin, HotelsAdmin, RoomsAdmin, UserAdmin
from app.bookings.dao import BookingDAO
from app.bookings.router import router as router_bookings
from app.database import engine
from app.exceptions import RoomCannotBeBooked

from app.images.router import router as router_images
from app.pages.router import router as router_pages
from app.hotels.router import router as router_hotels
from app.rooms.router import router as router_rooms
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.router import router as router_users
from app.logger import logger
from app.rooms.router import get_rooms
from app.utils import format_number_thousand_separator


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost:6379")
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield


app = FastAPI(lifespan=lifespan)

import sentry_sdk

#отслеживаем ошибки
sentry_sdk.init( 
    dsn="https://a891116025679a5aa85f4932d59163cb@o4508276436303872.ingest.de.sentry.io/4508276445085776",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_pages)
app.include_router(router_images)
app.include_router(router_rooms)


app.mount("/static", StaticFiles(directory="app/static"), "static")

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_creedntails=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Coontent-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Authorization",
    ],
)


class HotelSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


templates = Jinja2Templates(directory="app/templates")
@app.get("/", response_class=HTMLResponse)
async def get_home_page(
    request: Request,
    rooms=Depends(get_rooms)
    ):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "rooms":rooms,
            }
        )

# @app.get("/hotels")
# def get_hotels(search_args: HotelSearchArgs = Depends()):
#     return search_args

admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)
admin.add_view(UserAdmin)
admin.add_view(BookingsAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(
        "Request handling time ", extra={"process_time": round(process_time, 4)}
    )
    return response
