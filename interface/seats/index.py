from custom_types import CinemaHall

from interface.view.index import show_hall
from interface.view.custom_input import custom_input

from tools.seats.index import get_seat_status
from tools.view.index import numbers_into_letters, letters_into_numbers

from constants.index import SEAT_ICON


def input_coords_seat(hall: list[list]):
    """Retorna las coordenadas de una butaca"""
    total_rows = len(hall)
    total_cols = len(hall[0])

    while True:
        row = int(input(f"Ingrese la FILA (1-{total_rows}): "))
        if row < 1 or row > total_rows:
            print("Fila fuera de rango.")
            continue

        col = input(
            f"Ingrese la COLUMNA (A-{numbers_into_letters(total_cols - 1)}) para la fila {row}: "
        ).upper()
        col_index = letters_into_numbers(col)

        if col_index + 1 > total_cols:
            print("Columna fuera de rango.")
            continue

        return (row - 1, col_index)


# no implementado
from interface.view.custom_input import custom_input


def input_seat_row(hall: list[list]):
    total_rows = len(hall)

    row = custom_input(
        f"Ingrese la FILA (1-{total_rows}, -1 para cancelar): ",
        int,
        validator=lambda row: (
            ("Fila fuera de rango.", None)
            if (row < 1 and row != -1) or row > total_rows
            else (None, row - 1)
        ),
    )

    return row


def input_seat_column(hall: list[list]):
    total_cols = len(hall[0])

    column = custom_input(
        f"Ingrese la COLUMNA (1-{total_cols}, -1 para cancelar) para la fila: ",
        int,
        validator=lambda column: (
            ("Columna fuera de rango.", None)
            if (column < 1 and column != -1) or column > total_cols
            else (None, column - 1)
        ),
    )
    if column == -1:
        return -1, -1

    return column


def input_seat_coords_whit_custom_input(hall: list[list]):
    """Retorna las coordenadas de una butaca"""
    row = input_seat_row(hall)
    if row == -1:
        return -1, -1

    column = input_seat_column(hall)
    if row == -1:
        return -1, -1

    return row, column


def input_free_seat(hall: list[list]):
    """Pide una butaca hasta que sea válida (libre). Devuelve (row, column)"""

    while True:
        show_hall(hall)

        row, column = input_coords_seat(hall)
        row_label, col_label = row + 1, column + 1

        status = get_seat_status(hall[row][column])

        if status is None:
            print(f"La butaca F{row_label}-C{col_label} está inhabilitada.")
            continue
        if status is False:
            print(f"La butaca F{row_label}-C{col_label} está ocupada.")
            continue

        return row, column


# no implementada
from interface.seats.index import input_seat_column


def input_free_seat_whit_custom_input(hall: list[list]):
    """Pide una butaca hasta que sea válida (libre). Devuelve (row, column)"""

    while True:
        show_hall(hall)

        # falta completar, validar si el usuario cancela
        row = input_seat_column(hall)

        row, column = input_coords_seat(hall)
        row_label, col_label = row + 1, column + 1

        status = get_seat_status(hall[row][column])

        if status is None:
            print(f"La butaca F{row_label}-C{col_label} está inhabilitada.")
            continue
        if status is False:
            print(f"La butaca F{row_label}-C{col_label} está ocupada.")
            continue

        return row, column


def find_first_free_seats(hall: CinemaHall, cantidad: int):
    free_seats = []
    for i in range(len(hall)):
        fila = hall[i]
        
        for j in range(len(fila)):
            asiento = hall[i][j]
            
            if asiento == SEAT_ICON:
                free_seats.append((i, j))
                
                if len(free_seats) == cantidad:
                    return free_seats
    return free_seats
