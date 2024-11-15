from pydantic import BaseModel


class SRooms(BaseModel):
    id :int
    hotel_id:int
    name :str
    description :str
    price :int
    services :str # In db its json ?
    quantity:int
    image_id : int



    class Config:
        #orm_mode= True
        from_attributes = True
