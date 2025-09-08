from interface.view.custom_input import custom_input
from typing import Literal

from interface.view.clear_screen import clear_screen

from interface.admin_halls_interface import admin_halls_interface


def admin_interface(
    all_halls: list[list], all_films: list[str]
) -> tuple[list[list], list[str], str, Literal[1, -10]]:
    while True:
        print("\n")

        print(
            f"""\tPanel de administración.

salas totales: {all_halls.__len__()}
              
1 - Entrar en modo usuario
2 - Administrar salas

10 - Apagar\n"""
        )

        options_tuple = (1, 2, 3, 10)
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
            break

        if admin_input == 2:
            admin_halls_interface(all_halls, all_films)

        if admin_input == 10:
            break

    clear_screen()
    return all_halls, all_films, admin_input
