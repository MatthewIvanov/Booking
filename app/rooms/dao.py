
from app.dao.base import BaseDAO
from app.rooms.models import Rooms


class RoomsDAO(BaseDAO):
    model = Rooms