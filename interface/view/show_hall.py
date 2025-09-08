# from custom_types import CinemaHall

from tools.view.index import calculate_width
from interface.view.show_columns import show_columns
from interface.view.show_rows import show_rows


# def show_hall(hall: CinemaHall):
#     if not hall or not hall[0]:
#         print("Sala de Cine (sin butacas)")
#         return

#     width_seat, width_row, width_total = calculate_width(hall)

#     print("Sala de Cine".center(width_total))
#     show_columns(len(hall[0]), width_row)
#     show_rows(hall, width_seat, width_row)
