import json
from typing import Any


def read_json(file_name: str) -> Any:
    try:
        with open(file_name, mode="rt", encoding="utf-8") as file:
            data = json.load(file)
    except OSError:
        print('"No se encuentra el archivo"')
    return data
