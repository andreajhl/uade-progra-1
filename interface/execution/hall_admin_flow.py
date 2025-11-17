from constants.index import MOVIE_PATH
from custom_types import CinemaHall, MoviesDatabase
from tools.display.index import clear_screen
from tools.movies.index import get_movie_by_id, delete_movie
from tools.json.index import save_json
from interface.core.hall_operations import (
    change_seat_status,
    clear_all_occupied_seats
)
from interface.ui.display import (
    display_hall_admin_header,
    display_hall_details,
    display_hall_admin_options,
    display_seat_status_options
)
from interface.ui.input import (
    get_hall_admin_choice,
    get_seat_status_choice,
    get_seat_coordinates,
    get_new_film_name_input
)
from tools.logs.index import write_log

def run_hall_admin_interface(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """Flujo principal de administración de sala."""
    data_changed = False 
    
    while True:
        movie = get_movie_by_id(movies_db, movie_id)
        if not movie:
            print(f"❌ Película con ID {movie_id} no encontrada")
            break
            
        hall = movie["hall"]
        film_name = movie["title"]
        
        show_hall_admin_state(hall, film_name)
        
        admin_choice = get_hall_admin_choice()
        
        if admin_choice == 1:
            handle_seat_status_change(hall)
            movies_db[movie_id] = {
                "title": movie["title"],
                "hall": hall,
                "category": movie["category"],
                "classification": movie["classification"],
                "schedule": movie["schedule"]
            }
            data_changed = True
        elif admin_choice == 2:
            movies_db = handle_film_name_change(movies_db, movie_id)
            data_changed = True
        elif admin_choice == 3:
            handle_clear_occupied_seats(hall)
            movies_db[movie_id] = {
                "title": movie["title"],
                "hall": hall,
                "category": movie["category"],
                "classification": movie["classification"],
                "schedule": movie["schedule"]
            }
            data_changed = True
        elif admin_choice == 4:
            movies_db = delete_movie(movies_db, movie_id)
            print(f"\n🗑️ Película '{film_name}' eliminada exitosamente")
            data_changed = True
            input("\n📌 Presione Enter para continuar...")
            break
        elif admin_choice == 9:
            break
            
        clear_screen()
    
    if data_changed:
        save_json(movies_db,MOVIE_PATH)
    
    return movies_db


def show_hall_admin_state(hall: CinemaHall, film_name: str) -> None:
    """Muestra el estado de administración de sala."""
    display_hall_admin_header(film_name)
    display_hall_details(hall)
    display_hall_admin_options()


def handle_seat_status_change(hall: CinemaHall) -> None:
    """Maneja cambio de estado de butaca."""
    row, column = get_seat_coordinates(hall)
    display_seat_status_options()
    status_choice = get_seat_status_choice()
    change_seat_status(hall, row, column, status_choice)


def handle_film_name_change(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """Maneja cambio de nombre de película."""
    new_name = get_new_film_name_input()
    
    movie = get_movie_by_id(movies_db, movie_id)
    if movie:
        write_log(f"Se modifico el titulo de la pelicula {movie["title"]} por {new_name}")
        movies_db[movie_id] = {
            "title": new_name,
            "hall": movie["hall"],
            "category": movie["category"],
            "classification": movie["classification"],
            "schedule": movie["schedule"]
        }
        print(f"\n✅ Título de película actualizado a: '{new_name}'")
    
    return movies_db


def handle_clear_occupied_seats(hall: CinemaHall) -> None:
    """Limpia todas las butacas ocupadas."""
    clear_all_occupied_seats(hall)
    write_log("Se limpiaron todas las butacas ocupadas")