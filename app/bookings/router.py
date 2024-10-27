
from fastapi import APIRouter
from sqlalchemy import select
from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings
from app.bookings.schemas import SBooking
from app.database import async_session_maker


router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование']
)


@router.get('')
async def get_bokings()->list[SBooking]:
   return await BookingDAO.find_all()
 
