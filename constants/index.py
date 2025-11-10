from pathlib import Path 

DISABLED_SEAT_ICON = " "
BUSY_SEAT_ICON = "⬛️"
RESERVED_SEAT_ICON = "⭕️"
SEAT_ICON = "⬜️"

BASE_DIR = Path(__file__).resolve().parent.parent

MOVIE_PATH = BASE_DIR / "movie.json"
CLASSIFICATION_PATH = BASE_DIR / "classification.json"
CATEGORY_PATH = BASE_DIR / "category.json"
USER_PATH = BASE_DIR / "users.json"

HALLS_NAME_IN_FILE = "halls"
FILMS_NAMES_IN_FILE = "films_names"

DEFAULT_CLASSIFICATION = {
  1: "Apta para todo público",
  2: "Mayores de 13 años",
  3: "Mayores de 16 años",
  4: "Mayores de 18 años"
}

DEFAULT_CATEGORY = {
  1: "Comedia/Fantasía",
  2: "Drama/Romance", 
  3: "Acción/Aventura",
  4: "Terror/Suspenso"
}