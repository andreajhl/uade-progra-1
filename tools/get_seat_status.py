from constants.index import DISABLED_SEAT_ICON, BUSY_SEAT_ICON

get_seat_status = lambda seat: (
    None if seat == DISABLED_SEAT_ICON else (False if seat == BUSY_SEAT_ICON else True)
)
