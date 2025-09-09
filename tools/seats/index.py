from typing import Callable
from custom_types import CinemaHall
from constants.index import DISABLED_SEAT_ICON, BUSY_SEAT_ICON, SEAT_ICON


# cambiar nombre a count_seats
def count_free_seats(
    hall: CinemaHall, custom_filter: Callable = lambda seat: seat == SEAT_ICON
):
    """Retorna la cantidad de butacas libres."""

    free_total = 0
    for row in hall:
        for seat in row:
            if custom_filter(seat):
                free_total += 1
    return free_total


def disable_seats(hall: list[list], row: int, column: int):
    """Marca una butaca como deshabilitada."""
    hall[row][column] = DISABLED_SEAT_ICON


get_seat_status = lambda seat: (
    None if seat == DISABLED_SEAT_ICON else (False if seat == BUSY_SEAT_ICON else True)
)


def set_busy_seat(row: int, col: int, hall: list[list]):
    hall[row][col] = BUSY_SEAT_ICON


def maximum_consecutive_in_matrix(matrix: list[list], element) -> int:
    count = 0
    result = 0

    for row in matrix:
        for row_element in row:

            if row_element == element:
                count += 1

        if count > result:
            result = count

        count = 0

    return result
