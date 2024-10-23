from datetime import date
from typing import Optional
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel

app=FastAPI()



class HotelSearchArgs:
     def __init__(
               self,
                location:str,
                date_from:date,
                date_to:date,
                has_spa:Optional[bool] = None,
                stars:Optional[int]=Query(None,ge=1,le=5)
            ):
               self.location=location
               self.date_from=date_from
               self.date_to=date_to
               self.has_spa=has_spa
               self.stars=stars

class SHotels(BaseModel):
    address:str
    name:str
    stars:int

@app.get('/hotels')
def get_hotels(
    search_args:HotelSearchArgs=Depends()
    ):
       return search_args



class SBooking(BaseModel):
    room_id:int
    date_from:int
    date_to:int
    
@app.post('/booking')
def add_booking(booking:SBooking):
    pass