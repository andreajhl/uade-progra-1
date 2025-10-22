
from custom_types import CinemaHall
from tools.display.index import show_hall
from tools.input.index import custom_input
from tools.view.index import numbers_into_letters, letters_into_numbers, validate_a_Z_string
from constants.index import SEAT_ICON, DISABLED_SEAT_ICON, BUSY_SEAT_ICON


count_seats = lambda hall, custom_filter=lambda seat: seat == SEAT_ICON: sum(
    1 for row in hall for seat in row if custom_filter(seat)
)
"""Retorna la cantidad de butacas libres."""


def set_seat_status(row: int, col: int, hall: list[list], icon=BUSY_SEAT_ICON):
    """Cambia de estado la butaca del asiento solicitado (fila, columna, icon(estado al que quiero modificar))"""
    hall[row][col] = icon


get_seat_status = lambda seat: (
    None if seat == DISABLED_SEAT_ICON else (False if seat == BUSY_SEAT_ICON else True)
)
"""Devuelve el estado de la butaca indicada (None si desabilitada, False si ocupado, True si libre)"""


def maximum_consecutive_in_matrix(matrix: list[list], element) -> int:
    """Devuelve el numero de veces que se repite consecutivamente el elemento en la matriz (Matriz, Elemento)"""
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


def get_coords_seat(hall: list[list]) -> tuple[int, int]:
    """
    Gets seat coordinates from user input.
    Returns (row, column) tuple.
    """
    total_rows = len(hall)
    total_cols = len(hall[0])

    def col_validator(col: str):
        col = col.upper()
        is_dec = col.isdecimal()
        are_letters = validate_a_Z_string(col)

        if not (is_dec or are_letters):
            return (ValueError("Valor invalido."), None)

        col_index = int(col) - 1 if is_dec else letters_into_numbers(col.upper())

        if col_index + 1 > total_cols:
            return (IndexError("Columna fuera de rango."), None)

        return (None, col_index)

    while True:
        row = custom_input(
            f"Ingrese la FILA (1-{total_rows}): ",
            int,
            validator=lambda row: (
                (IndexError("Fila fuera de rango."), None)
                if row < 1 or row > total_rows
                else (None, row)
            ),
        )

        col_index = custom_input(
            f"Ingrese la COLUMNA (A-{numbers_into_letters(total_cols - 1)}) para la fila {row}: ",
            str,
            validator=col_validator,
        )

        return row - 1, col_index


def get_free_seat(hall: list[list]) -> tuple[int, int]:
    """
    Asks for a seat until it's valid (free).
    Returns (row, column) tuple.
    """
    while True:
        show_hall(hall)

        row, column = get_coords_seat(hall)
        row_label, col_label = row + 1, column + 1

        status = get_seat_status(hall[row][column])

        if status is None:
            print(f"La butaca F{row_label}-C{col_label} está inhabilitada.")
            continue
        if status is False:
            print(f"La butaca F{row_label}-C{col_label} está ocupada.")
            continue

        return row, column


def get_first_free_seats(hall: CinemaHall, quantity: int) -> list[tuple[int, int]]:
    """
    Finds the first free seats in the hall.
    
    Args:
        hall: Cinema hall structure
        cantidad: Number of seats needed
        
    Returns:
        List of (row, column) tuples for free seats
    """
    for i in range(len(hall)):
        consecutive_seats = []
        row = hall[i]

        for j in range(len(row)):
            seat = hall[i][j]
            if seat == SEAT_ICON:
                consecutive_seats.append((i, j))
                if len(consecutive_seats) == quantity:
                    return consecutive_seats
    return consecutive_seats