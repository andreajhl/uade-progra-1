from custom_types import CinemaHall

from interface.view.custom_input import custom_input

from interface.seats.index import input_free_seat
from tools.seats.index import set_busy_seat
from interface.view.index import show_hall
from interface.view.index import clear_screen

def find_first_free_seats(hall: CinemaHall, cantidad: int):
    free_seats = []
    for i, fila in enumerate(hall):
        for j, asiento in enumerate(fila):
            if not asiento: 
                free_seats.append((i, j))
                if len(free_seats) == cantidad:
                    return free_seats
    return free_seats

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
        print(f"F{fila+1}-C{col+1}", end=" ")
    print()
    
    aceptar = custom_input(
        "¿Desea aceptar estas butacas? (si/no): ",
        str,
        validator=lambda x: (None, x.lower()) if x.lower() in ["si", "no"] else ("Ingrese 'si' o 'no'.", None)
    )

    if aceptar == "si":
        for fila, col in first_free_seats:
            set_busy_seat(fila, col, hall)
        print(f"Compra finalizada. Entradas adquiridas: {ticket_requested}.")
        show_hall(hall)
        return

    purchased = 0

    while purchased < ticket_requested:
        row, column = input_free_seat(hall)
        set_busy_seat(row, column, hall)

        print(f"Seleccionaste la butaca F{row+1}-C{column+1}.")

        purchased += 1

    print(f"Compra finalizada. Entradas adquiridas: {purchased}.")
    show_hall(hall)
