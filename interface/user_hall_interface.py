from custom_types import CinemaHall

from interface.custom_input import custom_input

from interface.input_free_seat import input_free_seat
from tools.set_busy_seat import set_busy_seat
from interface.show_hall import show_hall
from interface.clear_screen import clear_screen


def user_hall_interface(hall: CinemaHall, film_name: str, total_free: int):
    clear_screen()
    # quedaria mejor creando una funcion validadora aparte y pasandola como valor en validator pero necesitaria usar
    # el parametro validator_params de custom_input para pasar como parametro free_total a la hora de llamar al
    # validador y este parametro usa un diccionario, aparte su funcionamiento (args y kwargs) creo que no se vio en clase
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
