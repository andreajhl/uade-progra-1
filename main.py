from interface.init_interface import init_interface

from interface.admin_interface import admin_interface
from interface.user_interface import user_interface

def main():
    
    hall, film_name, admin_password = init_interface()
    
    all_halls = [hall]
    all_films = [film_name]

    while True:
        all_halls, all_films, admin_password, option = admin_interface(all_halls, all_films, admin_password)

        # entrar interfaz usuario
        if option == 1:
            while True:
                    
                all_halls, try_admin_password = user_interface(all_halls, all_films)

                if try_admin_password == admin_password:
                    break
        # salir
        elif option == -10:
            break

if __name__ == "__main__":
    main()