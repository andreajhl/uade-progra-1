from custom_types import CinemaHall

from interface.view.custom_input import custom_input

from interface.seats.index import input_free_seat, find_first_free_seats
from tools.seats.index import set_seat_status
from interface.view.index import show_hall
from interface.view.index import clear_screen

from constants.index import SEAT_ICON, RESERVED_SEAT_ICON


def user_hall_interface(hall: CinemaHall, film_name: str, total_free: int):
    clear_screen()

    print(film_name)
    ticket_requested = custom_input(
        f"Ingrese el número de entradas a comprar (disponibles: {total_free}): ",
        int,
        validator=lambda requested: (
            ("La cantidad debe ser mayor que 0.", None)
            if requested < 1
            else (
                (f"No hay suficientes butacas libres. Disponibles: {total_free}.", None)
                if requested > total_free
                else (None, requested)
            )
        ),
    )

    first_free_seats = find_first_free_seats(hall, ticket_requested)
    if len(first_free_seats) < ticket_requested:
        print("No hay suficientes butacas libres.")
        return

    print("Las siguientes butacas están disponibles para usted:")
    for fila, col in first_free_seats:
        set_seat_status(fila, col, hall, RESERVED_SEAT_ICON)
    show_hall(hall)

    aceptar = custom_input(
        "¿Desea aceptar estas butacas? (1 = si/ 2 = no): ",
        int,
        validator=lambda x: (
            (None, x) if x in [1, 2] else ("Ingrese '1 = si' o '2 = no'.", None)
        ),
    )

    if aceptar == 1:
        for fila, col in first_free_seats:
            set_seat_status(fila, col, hall)

        print(f"Compra finalizada. Entradas adquiridas: {ticket_requested}.")

        show_hall(hall)
        return
    else:
        for fila, col in first_free_seats:
            set_seat_status(fila, col, hall, SEAT_ICON)

    purchased = 0

    while purchased < ticket_requested:
        row, column = input_free_seat(hall)
        set_seat_status(row, column, hall)

        print(f"Seleccionaste la butaca F{row+1}-C{column+1}.")

        purchased += 1

    print(f"Compra finalizada. Entradas adquiridas: {purchased}.")
    show_hall(hall)
