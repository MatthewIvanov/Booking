
from sqladmin import ModelView

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.rooms.models import Rooms
from app.users.models import Users


class UserAdmin(ModelView, model= Users):
     column_list=[Users.id,Users.email]
     column_details_exclude_list=[]
     can_delete=False
     name= 'Пользователь'
     name_plural='Пользователи'
     icon = "fa-solid fa-user"


class BookingsAdmin(ModelView, model= Bookings):
     column_list=[columns for columns in Bookings.__table__.columns] + [Bookings.user,Bookings.room_id]
     name= 'Бронь'
     name_plural='Брони'



class HotelsAdmin(ModelView,model=Hotels):
     column_list=[columns for columns in Hotels.__table__.columns] + [Hotels.rooms]
     name= 'Отель'
     name_plural='Отели'
     icon = 'fa-solid fa-hotel'

class RoomsAdmin(ModelView,model=Rooms):
     column_list=[columns for columns in Rooms.__table__.columns] + [Rooms.hotel,Rooms.booking]
     name= 'Номер'
     name_plural='Номера'
     icon = 'fa-solid fa-hotel'     
   