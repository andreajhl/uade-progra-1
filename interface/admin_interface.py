from interface.view.custom_input import custom_input
from typing import Literal

from interface.view.index import clear_screen

from interface.show_halls import show_halls
from interface.admin_hall_interface import admin_hall_interface

from interface.halls.index import init_hall


def admin_interface(
    all_halls: list[list], all_films_names: list[str]
) -> tuple[list[list], list[str], str, Literal[1, 9]]:
    """Despliega menu para entrar en modo usuario o administrar las Salas"""
    while True:
        print("\tPanel de administración.")
        show_halls(all_halls, all_films_names)

        print(
            f"""
salas totales: {all_halls.__len__()}

-1 - Entrar en modo usuario
-2 - Crear sala
-9 - Apagar\n"""
        )

        halls_indexes = range(all_halls.__len__())

        admin_input = custom_input(
            "Elija una sala: ",
            int,
            error_message="Opcion invalida.",
            validator=lambda option: (
                ("Opcion invalida.", None)
                if not ((option - 1) in halls_indexes) and not (option in (-1, -2, -9))
                else (None, option)
            ),
        )

        if admin_input == -2:
            all_halls.append(init_hall())
            all_films_names.append(custom_input("En esta sala se proyectara: ", str))
            clear_screen()
            continue

        if admin_input in (-1, -9):
            break

        hall_selected_index = admin_input - 1
        if hall_selected_index in halls_indexes:
            clear_screen()
            all_halls, all_films_names = admin_hall_interface(
                all_halls, all_films_names, hall_selected_index
            )

    clear_screen()
    return all_halls, all_films_names, admin_input
