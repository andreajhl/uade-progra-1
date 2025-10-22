

from custom_types import MoviesDatabase
from tools.display.index import clear_screen
from tools.movies.index import (
    get_movies_count,
    get_all_movie_ids,
    get_movie_by_id
)
from interface.ui.display import display_user_welcome, display_movies_overview
from interface.ui.input import get_user_menu_choice_movies
from tools.json.index import save_json


def run_user_interface(movies_db: MoviesDatabase) -> MoviesDatabase:
    """Flujo principal de interfaz de usuario."""
    data_changed = False
    
    while True:
        show_user_menu_state(movies_db)
        
        user_choice = get_user_menu_choice_movies(get_movies_count(movies_db))
        
        if user_choice == 9:
            break
            
        movie_ids = get_all_movie_ids(movies_db)
        if user_choice > 0 and user_choice <= len(movie_ids):
            movie_index = user_choice - 1
            movie_id = movie_ids[movie_index]
            movies_db = handle_movie_selection(movies_db, movie_id)
            data_changed = True
            
        clear_screen()
    
    if data_changed:
        save_json(movies_db)
    
    clear_screen()
    return movies_db


def show_user_menu_state(movies_db: MoviesDatabase) -> None:
    """Muestra el estado del menú de usuario."""
    display_user_welcome()
    display_movies_overview(movies_db)


def handle_movie_selection(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """Maneja selección de película para compra de entradas."""
    movie = get_movie_by_id(movies_db, movie_id)
    if not movie:
        print(f"❌ Película con ID {movie_id} no encontrada")
        return movies_db
    
    from interface.execution.ticket_flow import run_ticket_purchase_interface
    return run_ticket_purchase_interface(movies_db, movie_id)