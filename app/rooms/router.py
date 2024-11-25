
from datetime import date, datetime, timedelta
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from fastapi_cache.decorator import cache

from app.rooms.dao import RoomsDAO
from app.rooms.shemas import SRoomsInfo

router = APIRouter(prefix="/rooms", tags=["Комнаты"])

@router.get("")
@cache(expire=2000)
async def get_rooms():
    return await RoomsDAO.find_all()

@router.get("/search")
async def search_rooms():
    pass

@cache(expire=2000)
@router.get("/{hotel_id}/rooms")
async def get_rooms_by_time(
    hotel_id: int,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
) -> List[SRoomsInfo]:
    rooms = await RoomsDAO.find_all_filter(hotel_id, date_from, date_to)
    return rooms
