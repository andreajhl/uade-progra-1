from custom_types import CinemaHall, MoviesDatabase
from interface.controllers.admin_interface import admin_interface
from interface.controllers.user_interface import user_interface
from tools.input.index import custom_input
from tools.display.index import clear_screen
from tools.movies.index import create_or_get_movies_database
from tools.loggin.main_loggin import loggin


def init_interface() -> None:
    """Punto de entrada principal de la aplicación."""
    clear_screen()

    print("🎬" * 20)
    print("    BIENVENIDO A CINEPLAY")
    print("🎬" * 20)

    movies_db: MoviesDatabase = create_or_get_movies_database()

    while True:
        print("\n" + "=" * 40)
        print("         MENÚ PRINCIPAL")
        print("=" * 40)
        print("1. Panel de Administrador")
        print("2. Interface de Usuario")
        print("3. Salir")
        print("=" * 40)

        option = custom_input(
            "Seleccione una opción: ",
            int,
            validator=lambda option: (
                (None, option)
                if 1 <= option <= 3
                else ("Opción inválida. Seleccione entre 1 y 3.", None)
            ),
        )

        if option == 1:
            print("\n🔧 Accediendo al Panel de Administrador...")
            success = loggin()

            if not success:
                print("\n🚫 Inicio de sesión fallido. Volviendo al menú principal...")
                input("Presione Enter para continuar...")
                clear_screen()
                continue  # vuelve al menú principal

            movies_db = admin_interface(movies_db)

        elif option == 2:
            print("\n👤 Accediendo a la Interface de Usuario...")

            from tools.movies.index import get_movies_count

            if get_movies_count(movies_db) == 0:
                print("\n" + "=" * 50)
                print("🎭 No hay películas disponibles en este momento")
                print("=" * 50)
                print("📝 Por favor, acceda al Panel de Administrador")
                print("   para crear películas.")
                print("=" * 50)
                input("\n📌 Presione Enter para volver al menú principal...")
                clear_screen()
                continue

            movies_db = user_interface(movies_db)

        elif option == 3:
            print("\n👋 ¡Gracias por usar CinePlay!")
            print("🎬 ¡Hasta la próxima!")
            break
