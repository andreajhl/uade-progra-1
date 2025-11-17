import os
from datetime import datetime

LOG_PATH = "admin_log.txt"


def write_log(message: str) -> None:
    """Agrega una entrada al archivo de log con fecha y hora."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_PATH, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


def read_log() -> list[str]:
    """Lee el archivo de log y devuelve la lista de líneas."""
    if not os.path.exists(LOG_PATH):
        return []

    with open(LOG_PATH, "r", encoding="utf-8") as file:
        return file.readlines()
