from interface.view.custom_input import custom_input
from tools.halls.index import create_halls
from tools.seats.index import get_seat_status, set_seat_status
from custom_types import CinemaHall
from constants.index import DISABLED_SEAT_ICON
from interface.seats.index import input_coords_seat
from interface.view.index import show_hall


def init_hall():
    """Crea la sala de cine"""

    # Establecer filas y columnas
    rows: int = custom_input(
        "Ingresa el numero de filas que tendra la sala: ",
        int,
        validator=lambda rows: (None, rows) if rows >= 1 else ("Minimo 1 fila", None),
    )

    columns: int = custom_input(
        "Ingresa el numero de columnas que tendra la sala: ",
        int,
        validator=lambda columns: (
            (None, columns) if columns >= 1 else ("Minimo 1 columna", None)
        ),
    )

    print()

    hall = create_halls(rows, columns)

    # Deshabilitar butacas
    option = None
    while option != 2:
        show_hall(hall)
        option: int = custom_input(
            input_message="¿Desea inhabilitar alguna butaca? (1=Sí, 2=No): ",
            input_type=int,
            validator=lambda inpt: (
                (None, inpt)
                if 1 == inpt or inpt == 2
                else ("Opción inválida. Ingrese 1 o 2.", None)
            ),
        )

        if option == 2:
            print("Finalizó la inhabilitación de butacas.")
            break

        row, column = input_coords_seat(hall)
        print()
        row_label = row + 1
        col_label = column + 1

        seat_status = get_seat_status(hall[row][column])

        if seat_status is None:
            print(
                f"La butaca {row_label}{col_label} ya está inhabilitada.", end="\n" * 2
            )
            continue

        if seat_status is False:
            print(
                f"No se puede inhabilitar: la butaca F{row_label}-C{col_label} está ocupada.",
                end="\n" * 2,
            )
            continue

        set_seat_status(row, column, hall, DISABLED_SEAT_ICON)
        print(
            f"Butaca F{row_label}-C{col_label} inhabilitada correctamente.",
            end="\n" * 2,
        )

    return hall
