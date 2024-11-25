from datetime import datetime
import pytest
from fastapi import status
from httpx import ASGITransport, AsyncClient
from pydantic import EmailStr

from app.bookings.dao import BookingDAO
from app.config import settings
from app.main import app as fastapi_app




@pytest.mark.parametrize("room_id,date_from,date_to,status_code",[
    ("1","2024-11-24","2024-11-24",200),
])


async def test_booking(room_id,date_from,date_to,status_code, ac:AsyncClient):
    response = await ac.post("/bookings",json={
        "room_id": room_id,
        "date_from": date_from,
        "date_to": date_to,
    })
    assert response.status_code==status_code



@pytest.mark.parametrize("user_id, room_id", [
    (2,2),
    (2,3),
    (1,4),
    (1,4),
])
async def test_booking_crud(user_id, room_id):
    # Добавление брони
    new_booking = await BookingDAO.add(
        user_id=user_id,
        room_id=room_id,
        date_from=datetime.strptime("2023-07-10", "%Y-%m-%d"),
        date_to=datetime.strptime("2023-07-24", "%Y-%m-%d"),
    )

    assert new_booking["user_id"] == user_id
    assert new_booking["room_id"] == room_id

    # Проверка добавления брони
    new_booking = await BookingDAO.find_one_or_none(id=new_booking.id)

    assert new_booking is not None

    # Удаление брони
    await BookingDAO.delete(
        id=new_booking["id"],
        user_id=user_id,
    )

    # Проверка удаления брони
    deleted_booking = await BookingDAO.find_one_or_none(id=new_booking["id"])
    assert deleted_booking is None
    