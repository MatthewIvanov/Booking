


from datetime import date, datetime
from fastapi import APIRouter, Query


router= APIRouter(
    prefix='/hotels',
    tags=['Отели']
)

# @router.get('')
# @cache(expire=300)
# async def get_hotels_by_location_and_time(
#     location:str,
#     date_from:date=Query(...,description=f'Например, {datetime.now().date()}'),
#     date_to:date = Query(...,description=f'Например, {datetime.now().date()}')
# ):
#     hotels: await HotelDAO.search_for_hotels(location,date_from,date_to)
#     hotels_json=parse_obj_as(List[HoteInfo],hotels)
#     return hotels_json

# @router.get('/{hotel_id}/rooms')
# async def get_rooms_by_time(
#     hotel_id:int,
#     date_from:date=Query(...,description=f'Например, {datetime.now().date()}'),
#     date_to:date=Query(...,description=f'Например, {datetime.now().date()}'),
# )->List[RoomInfo]:
#     rooms=await HotelDAO.search_for_rooms(hotel_id,date_from,date_to)
#     return rooms