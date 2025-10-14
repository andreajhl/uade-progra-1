from custom_types import CinemaHall
from interface.view.custom_input import custom_input
from interface.user_hall_interface import user_hall_interface
from interface.view.index import clear_screen
from interface.show_halls import show_halls
from tools.seats.index import count_seats, count_seats


def user_interface(all_halls: list[CinemaHall], all_films_names: list[str]):
    while True:
        print("\tBienvenido.")
        show_halls(all_halls, all_films_names)

        halls_indexes = range(all_halls.__len__())

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
            clear_screen()
            return all_halls

        hall_selected_index = user_input - 1
        if hall_selected_index in halls_indexes:
            user_hall_interface(
                all_halls[hall_selected_index],
                all_films_names[hall_selected_index],
                count_seats(all_halls[hall_selected_index]),
            )

        clear_screen()
