
from fastapi import APIRouter, Depends
from sqlalchemy import select
from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings
from app.bookings.schemas import SBooking
from app.database import async_session_maker
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование']
)


@router.get('')
async def get_bokings(user: Users=Depends(get_current_user))->list[SBooking]:
   return await BookingDAO.find_all(user_id=user.id)
 
