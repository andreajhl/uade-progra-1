from typing import Any


def write_json(file_name: str, data: Any):
    try:
        with open(file_name, mode="w") as file:
            file.write(data)
        return True
    except OSError:
        # TODO: agregar log de error
        return False
