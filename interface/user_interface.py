from constants.index import SEAT_ICON, BUSY_SEAT_ICON
from custom_types import CinemaHall
from interface.view.custom_input import custom_input
from interface.user_hall_interface import user_hall_interface
from interface.view.clear_screen import clear_screen
from interface.admin_halls_interface import admin_halls_interface
from tools.seats.index import count_free_seats
from tools.maximum_consecutive_in_matrix import maximum_consecutive_in_matrix

def user_interface(all_halls: list[CinemaHall], all_films_names: list[str]):
    while True:
        print(
            """\tBienvenido.
              
Catalogo:
        
Sala \t Pelicula \t Espacios \t Espacios consecutivos maximos"""
        )

        halls_indexes = range(all_films_names.__len__())
        for hall_index in halls_indexes:
            total_free_seats = count_free_seats(all_halls[hall_index])
            total_number_of_available_seats = count_free_seats(
                all_halls[hall_index], lambda seat: seat in [SEAT_ICON, BUSY_SEAT_ICON]
            )
            print(
                f"{hall_index+1} \t {all_films_names[hall_index]} \t {total_free_seats}/{total_number_of_available_seats} \t {maximum_consecutive_in_matrix(all_halls[hall_index], SEAT_ICON)}"
            )
        print()

        user_input = custom_input(
            "Elija una sala (9 para entrar en modo administrador): ",
            int,
            error_message="Opcion invalida.",
            validator=lambda option: (
                ("Opcion invalida.", None)
                if not (option - 1 in halls_indexes) and option != 9
                else (None, option)
            ),
        )

        if user_input == 9:
            admin_halls_interface(all_halls, all_films_names)
        else:
            hall_selected_index = user_input - 1
            if hall_selected_index in halls_indexes:
                user_hall_interface(
                    all_halls[hall_selected_index],
                    all_films_names[hall_selected_index],
                    count_free_seats(all_halls[hall_selected_index]),
                )

            clear_screen()
            return all_halls
