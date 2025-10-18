from pathlib import Path 

DISABLED_SEAT_ICON = " "
BUSY_SEAT_ICON = "⬛️"
RESERVED_SEAT_ICON = "🟦"
SEAT_ICON = "⬜️"

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data.json"

HALLS_NAME_IN_FILE = "halls"
FILMS_NAMES_IN_FILE = "films_names"