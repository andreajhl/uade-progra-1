# from interface.view.show_hall import show_hall
# from interface.seats.input_coords_seat import input_coords_seat
# from tools.seats.get_seat_status import get_seat_status


# def input_free_seat(hall: list[list]):
#     """Pide una butaca hasta que sea válida (libre). Devuelve (row, column)"""

#     while True:
#         show_hall(hall)

#         row, column = input_coords_seat(hall)
#         row_label, col_label = row + 1, column + 1

#         status = get_seat_status(hall[row][column])

#         if status is None:
#             print(f"La butaca F{row_label}-C{col_label} está inhabilitada.")
#             continue
#         if status is False:
#             print(f"La butaca F{row_label}-C{col_label} está ocupada.")
#             continue

#         return row, column


# # no implementada
# from interface.seats.input_coords_seat import input_seat_column


# def input_free_seat_whit_custom_input(hall: list[list]):
#     """Pide una butaca hasta que sea válida (libre). Devuelve (row, column)"""

#     while True:
#         show_hall(hall)

#         # falta completar, validar si el usuario cancela
#         row = input_seat_column(hall)

#         row, column = input_coords_seat(hall)
#         row_label, col_label = row + 1, column + 1

#         status = get_seat_status(hall[row][column])

#         if status is None:
#             print(f"La butaca F{row_label}-C{col_label} está inhabilitada.")
#             continue
#         if status is False:
#             print(f"La butaca F{row_label}-C{col_label} está ocupada.")
#             continue

#         return row, column
