"""
Initial interface controller - updated to show main menu immediately.
Entry point for the application, coordinates main menu and user type selection.
"""

from custom_types import CinemaHall, MoviesDatabase
from interface.controllers.admin_interface import admin_interface
from interface.controllers.user_interface import user_interface
from tools.input.custom_input import custom_input
from tools.display.hall_display import clear_screen
from tools.movies.movie_utils import create_empty_movies_database


def init_interface() -> None:
    """
    Main application entry point.
    Shows main menu immediately without forcing hall creation.
    Uses MoviesDatabase for proper movie management.
    """
    clear_screen()
    
    print("🎬" * 20)
    print("    BIENVENIDO AL SISTEMA DE CINE")
    print("🎬" * 20)
    
    # Initialize empty movies database
    movies_db: MoviesDatabase = create_empty_movies_database()
    
    # Main application loop with user profile selection
    while True:
        print("\n" + "="*40)
        print("         MENÚ PRINCIPAL")
        print("="*40)
        print("1. Panel de Administrador")
        print("2. Interface de Usuario")
        print("3. Salir")
        print("="*40)
        
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
            movies_db = admin_interface(movies_db)
                
        elif option == 2:
            print("\n👤 Accediendo a la Interface de Usuario...")
            
            # Check if there are any movies available
            from tools.movies.movie_utils import get_movies_count
            if get_movies_count(movies_db) == 0:
                print("\n" + "="*50)
                print("🎭 No hay películas disponibles en este momento")
                print("="*50)
                print("📝 Por favor, acceda al Panel de Administrador")
                print("   para crear películas.")
                print("="*50)
                input("\n📌 Presione Enter para volver al menú principal...")
                clear_screen()
                continue
            
            # Use MoviesDatabase directly
            movies_db = user_interface(movies_db)
            
        elif option == 3:
            print("\n👋 ¡Gracias por usar el Sistema de Cine!")
            print("🎬 ¡Hasta la próxima!")
            break
