from typing import Literal, List, TypedDict
from constants.index import DISABLED_SEAT_ICON, BUSY_SEAT_ICON, SEAT_ICON

SeatState = Literal[DISABLED_SEAT_ICON, BUSY_SEAT_ICON, SEAT_ICON]
CinemaHall = List[List[SeatState]]

MovieCategory = Literal["A", "B", "C", "D"]
AgeClassification = Literal["ATP", "+13", "+16", "+18"]

class Movie(TypedDict):
    """Estructura de información de película."""
    title: str
    hall: CinemaHall
    category: MovieCategory
    classification: AgeClassification
    schedule: str

MoviesDatabase = dict[str, Movie]
