from typing import Union
from constants.index import DATA_PATH
from custom_types import MoviesDatabase
from typing import Any
import json

from constants.index import DATA_PATH, HALLS_NAME_IN_FILE, FILMS_NAMES_IN_FILE


def write_json(file_path: str, data: Any):
    try:
        with open(file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)#ensure_ascii=False,

    except Exception as e:
        return e
    
def load_data():
    data, err = read_json(DATA_PATH)

    if err: return None, None

    return data[HALLS_NAME_IN_FILE], data[FILMS_NAMES_IN_FILE]

def read_json(file_path: str) -> Union[tuple[Any,  None], tuple[Exception, None]]:
  try:
      with open(file_path, mode="rt", encoding="utf-8") as file:
          return json.load(file), None
  except Exception as err:
      return None, err
  
def save_json(movies_db: MoviesDatabase) -> Union[Exception, None]:
    """
    Saves MoviesDatabase to JSON file.
    
    Args:
        movies_db: Movies database to save
        
    Returns:
        None if successful, Exception if failed
    """
    data = {
        "movies_database": movies_db
    }
    return write_json(DATA_PATH, data)