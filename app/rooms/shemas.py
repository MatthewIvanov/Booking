from typing import List, Optional
from pydantic import BaseModel


class SRooms(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: Optional[str] = " "
    price: int
    services: List[str]  # In db its json ?
    quantity: int
    image_id: int

    class Config:
        # orm_mode= True
        from_attributes = True


class SRoomsInfo(SRooms):
    total_cost: int
    rooms_left: int

    class Config:
        from_attributes = True
