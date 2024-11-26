import codecs
import csv
from datetime import datetime
import json
from typing import Iterable, Literal

from fastapi import APIRouter, Depends, UploadFile

from app.bookings.dao import BookingDAO
from app.hotels.dao import HotelsDAO
from app.rooms.dao import RoomsDAO
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix="/import",
    tags=["Импорт данных в БД"],
)


TABLE_MODEL_MAP = {
    "hotels": HotelsDAO,
    "rooms": RoomsDAO,
    "bookings": BookingDAO,
}


def convert_csv_to_postgres_format(csv_iterable: Iterable):
    try:
        data = []
        for row in csv_iterable:
            for k, v in row.items():
                if v.isdigit():
                    row[k] = int(v)
                elif k == "services":
                    row[k] = json.loads(v.replace("'", '"'))
                elif "date" in k:
                    row[k] = datetime.strptime(v, "%Y-%m-%d")
            data.append(row)
        return data
    except Exception:
        print("Cannot convert CSV into DB format")


@router.post(
    "/{table_name}",
    status_code=201,
    dependencies=[Depends(get_current_user)],
)
async def import_data_to_table(
    file: UploadFile,
    table_name: Literal["hotels", "rooms", "bookings"],
):
    ModelDAO = TABLE_MODEL_MAP[table_name]
    # file - сам файл, filename - название файла, size - размер файла.
    csvReader = csv.DictReader(codecs.iterdecode(file.file, "utf-8"), delimiter=";")
    data = convert_csv_to_postgres_format(csvReader)
    file.file.close()
    if not data:
        raise 502
    added_data = await ModelDAO.add_bulk(data)
    if not added_data:
        raise 502
