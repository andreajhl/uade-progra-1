from interface.view.custom_input import custom_input
from custom_types import CinemaHall
from interface.view.index import show_hall
from interface.seats.index import input_coords_seat
from constants.index import DISABLED_SEAT_ICON, SEAT_ICON, BUSY_SEAT_ICON
from interface.view.index import clear_screen


def admin_hall_interface(
    all_halls: list[CinemaHall], all_films_names: list[str], hall_id: int
) -> tuple[list[CinemaHall], list[str]]:
    while True:
        hall = all_halls[hall_id]
        film_name = all_films_names[hall_id]

        print("\tPanel de administración.")
        print(film_name)
        show_hall(hall)
        print()
        print(
            f"""1 - marcar como Ocupada/Deshabilitada/Habilitada una butaca
2 - Cambiar nombre de pelicula
3 - Limpiar todos los asientos ocupados

4 - Eliminar sala

9 - Atras\n"""
        )

        options_tuple = (1, 2, 3, 4, 9)
        admin_input = custom_input(
            "opcion: ",
            int,
            error_message="Opcion invalida.",
            validator=lambda option: (
                ("Opcion invalida.", None)
                if not (option in options_tuple)
                else (None, option)
            ),
        )

        if admin_input == 1:

            row, column = input_coords_seat(hall)
            print("Marcar como:")
            print("""1 - Habilitada\n2 - Ocupada\n3 - Deshabilitada\n""")

            set_seat_as = custom_input(
                "opcion: ",
                int,
                error_message="Opcion invalida.",
                validator=lambda option: (
                    ("Opcion invalida.", None)
                    if not (option in (1, 2, 3))
                    else (None, option)
                ),
            )

            if set_seat_as == 1:
                hall[row][column] = SEAT_ICON
            elif set_seat_as == 2:
                hall[row][column] = BUSY_SEAT_ICON
            else:
                hall[row][column] = DISABLED_SEAT_ICON

            clear_screen()
            continue

        if admin_input == 2:
            all_films_names[hall_id] = input("En esta sala se proyectará:")

            clear_screen()
            continue

        if admin_input == 3:
            for row_id in range(hall.__len__()):
                for col_id in range(hall[row_id].__len__()):
                    if hall[row_id][col_id] == BUSY_SEAT_ICON:
                        hall[row_id][col_id] = SEAT_ICON

            clear_screen()
            continue

        if admin_input == 4:
            all_halls.pop(hall_id)
            all_films_names.pop(hall_id)
            return all_halls, all_films_names

        if admin_input == 9:
            return all_halls, all_films_names
