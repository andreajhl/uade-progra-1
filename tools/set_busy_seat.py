from constants import BUSY_SEAT_ICON


def set_busy_seat(row: int, col: int, hall: list[list]):
    hall[row][col] = BUSY_SEAT_ICON
