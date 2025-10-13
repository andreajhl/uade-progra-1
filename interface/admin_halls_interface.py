from interface.view.custom_input import custom_input
from interface.halls.index import init_hall


def admin_halls_interface(
    all_halls: list[list], all_films: list[str]
) -> tuple[list[list], list[str]]:
    """Despliega la intefaz del administrado, permite crear salas, info salsa, actualizar salas, eliminar salas"""
    while True:
        print(
            f"""\tPanel de administración.
        
salas totales: {all_halls.__len__()}

1 - Crear nueva sala
2 - Info salas
3 - Actualizar sala
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
            all_halls.append(init_hall())
            all_films.append(custom_input("En esta sala se proyectara: ", str))  #

        if admin_input == 2:
            pass

        if admin_input == 3:
            pass

        if admin_input == 4:
            pass

        if admin_input == 9:
            return all_halls, all_films
