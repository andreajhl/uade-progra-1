from constants import DISABLED_SEAT_ICON


def disable_seats(hall: list[list], row: int, column: int):
    """Marca una butaca como deshabilitada."""
    hall[row][column] = DISABLED_SEAT_ICON
