from typing import Any
import json


def write_json(file_path: str, data: Any):
    try:
        with open(file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)#ensure_ascii=False,

    except Exception as e:
        return e
