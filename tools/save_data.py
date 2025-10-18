from typing import Union
from .write_json import write_json
from constants.index import DATA_PATH, HALLS_NAME_IN_FILE, FILMS_NAMES_IN_FILE
from custom_types import CinemaHall

def save_data(halls:list[CinemaHall], films_names:list[str] )->Union[Exception, None]:
    data = {
        HALLS_NAME_IN_FILE: halls,
        FILMS_NAMES_IN_FILE: films_names,
    }
    return write_json(DATA_PATH, data)