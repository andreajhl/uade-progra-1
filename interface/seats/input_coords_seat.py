import string
from interface.view.custom_input import custom_input
from tools.view.numbers_into_letters import numbers_into_letters
from tools.view.letters_into_numbers import letters_into_numbers


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
        f"Ingrese la COLUMNA (1-{total_cols}, -1 para cancelar) para la fila {row}: ",
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
