import asyncio
from datetime import date

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from pydantic import TypeAdapter, parse_obj_as
import pydantic
from sqlalchemy import select
from sqlalchemy.orm import object_mapper

from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings
from app.bookings.schemas import SBooking, SBookingInfo, SNewBooking
from app.database import async_session_maker
from app.exceptions import RoomCannotBeBooked
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/bookings", tags=["Бронирование"])


@router.get("/all")
# @cache(expire=2000)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookingInfo]:
    # await asyncio.sleep(3) тестирование кэша
    return await BookingDAO.find_all_with_images(user_id=user.id)


@router.post("")
async def add_booking(
    booking: SNewBooking,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(
        user.id, booking.room_id, booking.date_from, booking.date_to
    )
    if not booking:
        raise RoomCannotBeBooked

    booking_dict = {
        col.key: getattr(booking, col.key) for col in object_mapper(booking).columns
    }
    send_booking_confirmation_email.delay(booking_dict, user.email)
    return 200


@router.delete("/{booking_id}")
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    print(123)
    await BookingDAO.delete(id=booking_id, user_id=current_user.id)
