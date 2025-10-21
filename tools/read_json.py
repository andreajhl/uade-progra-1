import json
from typing import Any, Union


def read_json(file_path: str) -> Union[tuple[Any,  None], tuple[Exception, None]]:
    try:
        with open(file_path, mode="rt", encoding="utf-8") as file:
            return json.load(file), None
    except Exception as err:
        return None, err
