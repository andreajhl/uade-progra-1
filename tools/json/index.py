from typing import Union, Any
from constants.index import DATA_PATH, HALLS_NAME_IN_FILE, FILMS_NAMES_IN_FILE
from custom_types import MoviesDatabase
import json


def write_json(file_path: str, data: Any):
    try:
        with open(file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)#ensure_ascii=False,

    except Exception as e:
        return e
    

def read_json(file_path: str) -> Union[tuple[Any,  None], tuple[Exception, None]]:
  try:
      with open(file_path, mode="rt", encoding="utf-8") as file:
          return json.load(file), None
  except Exception as err:
      return None, err
  
def load_data():
    data, err = read_json(DATA_PATH)

    if err: return None, None

    return data[HALLS_NAME_IN_FILE], data[FILMS_NAMES_IN_FILE]

def save_json(movies_db: MoviesDatabase) -> None:
    """
    Saves MoviesDatabase to JSON file.
    Handles all errors internally and shows appropriate messages.
    
    Args:
        movies_db: Movies database to save
    """
    try:
        data = {
            "movies_database": movies_db
        }
        result = write_json(DATA_PATH, data)
        if result is None:
            print("💾 Datos guardados exitosamente")
        else:
            print(f"⚠️ Error al guardar datos: {result}")
    except Exception as e:
        print(f"⚠️ Error al guardar datos: {e}")