"""
Execution flow for user operations.
Coordinates between UI input/display and core business logic.
Updated to use MoviesDatabase instead of separate lists.
"""

from custom_types import MoviesDatabase
from tools.display.hall_display import clear_screen
from tools.movies.movie_utils import (
    get_movies_count,
    get_all_movie_ids,
    get_movie_by_id
)
from interface.ui.display import display_user_welcome, display_movies_overview
from interface.ui.input import get_user_menu_choice_movies


def run_user_interface(movies_db: MoviesDatabase) -> MoviesDatabase:
    """
    Main execution flow for user interface using MoviesDatabase.
    Handles movie selection for ticket purchasing.
    """
    while True:
        # Display user menu
        _show_user_menu_state(movies_db)
        
        # Get user choice
        user_choice = get_user_menu_choice_movies(get_movies_count(movies_db))
        
        # Handle admin mode switch
        if user_choice == 9:
            clear_screen()
            return movies_db
            
        # Handle movie selection
        movie_ids = get_all_movie_ids(movies_db)
        if user_choice > 0 and user_choice <= len(movie_ids):
            movie_index = user_choice - 1
            movie_id = movie_ids[movie_index]
            movies_db = _handle_movie_selection(movies_db, movie_id)
            
        clear_screen()


def _show_user_menu_state(movies_db: MoviesDatabase) -> None:
    """Shows the current user menu state using MoviesDatabase."""
    display_user_welcome()
    display_movies_overview(movies_db)


def _handle_movie_selection(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """Handles user movie selection for ticket purchase."""
    movie = get_movie_by_id(movies_db, movie_id)
    if not movie:
        print(f"❌ Película con ID {movie_id} no encontrada")
        return movies_db
    
    from interface.execution.ticket_flow import run_ticket_purchase_interface
    return run_ticket_purchase_interface(movies_db, movie_id)