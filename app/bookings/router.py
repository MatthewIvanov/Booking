
import asyncio
from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy import select
from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings
from app.bookings.schemas import SBooking
from app.database import async_session_maker
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.exceptions import RoomCannotBeBooked
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование']
)


@router.get('')
@cache(expire=2000)
async def get_bokings(user: Users=Depends(get_current_user))->list[SBooking]:
   await asyncio.sleep(3)
   return await BookingDAO.find_all(user_id=user.id)
 
@router.post('')
async def add_booking(
   room_id:int,date_from:date, date_to:date,
   user:Users=Depends(get_current_user),
):
   booking=await BookingDAO.add(user.id,room_id,date_from,date_to)
   if not booking:
      raise RoomCannotBeBooked