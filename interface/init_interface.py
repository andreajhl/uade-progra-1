from time import sleep


from interface.halls.index import init_hall

from interface.view.custom_input import custom_input

from interface.view.index import clear_screen


def init_interface():
    clear_screen()

    print("\tBienvenido.", end="\n" * 2)
    sleep(0.5)

    print(
        "Para iniciar el sistema crearemos la primera sala",
        end="\n" * 2,
    )

    print("Iniciemos la primera sala...", end="\n" * 2)
    hall = init_hall()
    print()

    film_name: str = custom_input("En esta sala se proyectara: ", str)  #
    print()

    clear_screen()

    return hall, film_name
