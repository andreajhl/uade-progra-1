from constants.index import SEAT_ICON
from custom_types import CinemaHall


def create_halls(rows: int, columns: int) -> CinemaHall:
    """Crea la sala de cine, solicita (Filas y columnas)"""

    seats = []

    for _ in range(rows):
        seats.append([SEAT_ICON] * columns)

    return seats
