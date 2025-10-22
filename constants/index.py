from pathlib import Path 

DISABLED_SEAT_ICON = " "
BUSY_SEAT_ICON = "⬛️"
RESERVED_SEAT_ICON = "⭕️"
SEAT_ICON = "⬜️"

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data.json"

HALLS_NAME_IN_FILE = "halls"
FILMS_NAMES_IN_FILE = "films_names"

FILM_CLASSIFICATION = {
  1: "Apta para todo público",
  2: "Mayores de 13 años",
  3: "Mayores de 16 años",
  4: "Mayores de 18 años"
}

FILM_CATEGORY = {
  1: "Comedia/Fantasía",
  2: "Drama/Romance", 
  3: "Acción/Aventura",
  4: "Terror/Suspenso"
}