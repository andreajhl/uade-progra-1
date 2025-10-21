from typing import Literal, List, TypedDict
from constants.index import DISABLED_SEAT_ICON, BUSY_SEAT_ICON, SEAT_ICON

# Seat and hall types
SeatState = Literal[DISABLED_SEAT_ICON, BUSY_SEAT_ICON, SEAT_ICON]
CinemaHall = List[List[SeatState]]

# Movie-related types
MovieCategory = Literal["A", "B", "C", "D"]
AgeClassification = Literal["ATP", "+13", "+16", "+18"]

class Movie(TypedDict):
    """Movie information structure."""
    title: str
    hall: CinemaHall
    category: MovieCategory
    classification: AgeClassification
    schedule: str

# Movies database type - dictionary mapping movie IDs to movies
MoviesDatabase = dict[str, Movie]
