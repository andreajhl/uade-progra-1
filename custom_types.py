from typing import Literal, List
from constants.index import DISABLED_SEAT_ICON, BUSY_SEAT_ICON, SEAT_ICON

SeatState = Literal[DISABLED_SEAT_ICON, BUSY_SEAT_ICON, SEAT_ICON]

CinemaHall = List[List[SeatState]]
