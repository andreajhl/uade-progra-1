from typing import Union, Any
from constants.index import MOVIE_PATH, HALLS_NAME_IN_FILE, FILMS_NAMES_IN_FILE
from custom_types import MoviesDatabase
import json


def write_json(file_path: str, data: Any):
    try:
        with open(file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        return e


def read_json(file_path: str) -> Union[tuple[Any,  None], tuple[Exception, None]]:
  try:
      with open(file_path, mode="rt", encoding="utf-8") as file:
          return json.load(file), None
  except Exception as err:
      return None, err

def save_json(db: Any, path:str) -> None:
    """Guarda base de datos de películas en archivo JSON."""
    try:
        data = db
        result = write_json(path, data)
        if result is None:
            print("💾 Datos guardados exitosamente")
        else:
            print(f"⚠️ Error al guardar datos: {result}")
    except Exception as e:
        print(f"⚠️ Error al guardar datos: {e}")