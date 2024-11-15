from datetime import date

from pydantic import BaseModel


class SHotels(BaseModel):

    id: int
    name : str
    location: str
    services :str # In db its json ?
    rooms_quantity : int
    image_id :int


    class Config:
        #orm_mode= True
        from_attributes = True
