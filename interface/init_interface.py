from time import sleep


from interface.init_hall import init_hall

from interface.custom_input import custom_input

from interface.clear_screen import clear_screen


def init_interface():
    clear_screen()

    print("\tBienvenido.", end="\n" * 2)
    sleep(0.5)

    print(
        "Para iniciar el sistema crearemos la primera sala y una contraseña de administrador.",
        end="\n" * 2,
    )

    print("Iniciemos la primera sala...", end="\n" * 2)
    hall = init_hall()
    print()

    film_name: str = custom_input("En esta sala se proyectara: ", str)  #
    print()

    print("Ahora definamos la contraseña.", end="\n" * 2)

    admin_password: str = custom_input("Ingrese una contraseña:", str)  #

    """
    # No implementado por ser molesto a la hora de testear
    import getpass
    while True:
        admin_password:str = getpass("Ingrese una contraseña.")
        admin_password2:str = getpass("Repita la contraseña.")
        
        if admin_password == admin_password2:
            break
    """

    clear_screen()

    return hall, film_name, admin_password
