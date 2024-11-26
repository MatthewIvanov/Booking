from datetime import date
from typing import Optional

from fastapi import Query
from pydantic import BaseModel


class SHotels(BaseModel):

    id: int
    name: str
    location: str
    services: str  # In db its json ?
    rooms_quantity: int
    image_id: int

    class Config:
        # orm_mode= True
        from_attributes = True


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
