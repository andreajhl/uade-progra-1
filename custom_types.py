from typing import Literal, List, TypedDict
from constants.index import DISABLED_SEAT_ICON, BUSY_SEAT_ICON, SEAT_ICON

SeatState = Literal[DISABLED_SEAT_ICON, BUSY_SEAT_ICON, SEAT_ICON]
CinemaHall = List[List[SeatState]]

MovieCategory = Literal[1, 2, 3, 4]
AgeClassification = Literal[1, 2, 3, 4]

class Movie(TypedDict):
    """Estructura de información de película."""
    title: str
    hall: CinemaHall
    category: MovieCategory
    classification: AgeClassification
    schedule: str

MoviesDatabase = dict[str, Movie]
