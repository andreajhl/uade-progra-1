from interface.init_interface import init_interface

from interface.admin_interface import admin_interface
from interface.user_interface import user_interface


def main():

    hall, film_name = init_interface()

    all_halls = [hall]
    all_films = [film_name]

    while True:
        all_halls, all_films, option = admin_interface(all_halls, all_films)

        # entrar interfaz usuario
        if option == 1:
            while True:

                all_halls = user_interface(all_halls, all_films)
        # salir
        elif option == -10:
            break


if __name__ == "__main__":
    main()
