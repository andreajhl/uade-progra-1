from custom_types import CinemaHall

from interface.view.custom_input import custom_input

from interface.seats.index import input_free_seat
from tools.seats.index import set_busy_seat
from interface.view.index import show_hall
from interface.view.index import clear_screen


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

    purchased = 0

    while purchased < ticket_requested:
        row, column = input_free_seat(hall)
        set_busy_seat(row, column, hall)

        print(f"Seleccionaste la butaca F{row+1}-C{column+1}.")

        purchased += 1

    print(f"Compra finalizada. Entradas adquiridas: {purchased}.")
    show_hall(hall)
