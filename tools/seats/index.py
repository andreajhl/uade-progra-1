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


def set_seat_status(row: int, col: int, hall: list[list], icon=BUSY_SEAT_ICON):
    hall[row][col] = icon


get_seat_status = lambda seat: (
    None if seat == DISABLED_SEAT_ICON else (False if seat == BUSY_SEAT_ICON else True)
)


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
