"""
Execution flow for admin operations.
Coordinates between UI input/display and core business logic.
Updated to use MoviesDatabase instead of separate lists.
"""

from custom_types import MoviesDatabase
from tools.display.index import clear_screen
from tools.movies.index import (
    get_movies_count,
    add_movie_to_database,
    get_all_movie_ids,
    get_movie_by_id
)
from interface.ui.display import (
    display_admin_menu_header,
    display_admin_menu_options,
    display_movies_overview,
    display_movie_selection_menu
)
from interface.ui.input import (
    get_admin_menu_choice_movies,
    get_complete_movie_data,
    get_movie_selection_choice
)
from tools.json.index import save_json


def run_admin_interface(movies_db: MoviesDatabase) -> MoviesDatabase:
    """
    Main execution flow for admin interface using MoviesDatabase.
    Handles movie management instead of separate halls and films lists.
    """
    data_changed = False  # Flag to track if any changes were made
    
    while True:
        # Display current state
        _show_admin_menu_state(movies_db)
        
        # Get user choice
        admin_choice = get_admin_menu_choice_movies(get_movies_count(movies_db))
        
        # Handle menu options
        if admin_choice == 1:
            # Create new movie
            movies_db = _handle_create_movie(movies_db)
            data_changed = True
            continue
            
        elif admin_choice == 2:
            # Handle edit movie submenu
            result = _handle_edit_movie_selection(movies_db)
            if result is not None:
                movies_db, changed = result
                if changed:
                    data_changed = True
            continue
            
        elif admin_choice == 9:
            break

    # Save data only if changes were made
    if data_changed:
        save_json(movies_db)
    
    clear_screen()
    return movies_db


def _show_admin_menu_state(movies_db: MoviesDatabase) -> None:
    """Shows the current admin menu state using MoviesDatabase."""
    display_admin_menu_header()
    display_movies_overview(movies_db)
    display_admin_menu_options(get_movies_count(movies_db))


def _handle_create_movie(movies_db: MoviesDatabase) -> MoviesDatabase:
    """Handles the creation of a new movie with complete data."""
    # Get complete movie data
    movie_data = get_complete_movie_data()
    
    # Create the hall
    from interface.core.hall_operations import create_new_hall
    new_hall = create_new_hall()
    
    # Add movie to database
    movies_db, movie_id = add_movie_to_database(
        movies_db,
        title=movie_data["title"],
        hall=new_hall,
        category=movie_data["category"],  # type: ignore
        classification=movie_data["classification"],  # type: ignore
        schedule=movie_data["schedule"]
    )
    
    print(f"\n✅ Película creada exitosamente: '{movie_data['title']}'")
    print(f"🎭 Categoría: {movie_data['category']}")
    print(f"🔞 Clasificación: {movie_data['classification']}")
    print(f"📅 Horario: {movie_data['schedule']}")
    print(f"🆔 ID: {movie_id}")
    
    input("\n📌 Presione Enter para continuar...")
    clear_screen()
    return movies_db


def _handle_movie_management(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """Handles editing and management of a specific movie."""
    movie = get_movie_by_id(movies_db, movie_id)
    if not movie:
        print(f"❌ Película con ID {movie_id} no encontrada")
        return movies_db
    
    # Use the hall admin interface for movie management
    from interface.execution.hall_admin_flow import run_hall_admin_interface
    return run_hall_admin_interface(movies_db, movie_id)


def _handle_edit_movie_selection(movies_db: MoviesDatabase) -> tuple[MoviesDatabase, bool] | None:
    """Handles the movie selection submenu for editing."""
    while True:
        clear_screen()
        display_movie_selection_menu(movies_db)
        
        movies_count = get_movies_count(movies_db)
        choice = get_movie_selection_choice(movies_count)
        
        if choice == 9:
            return None  # Go back to main menu
            
        # Handle movie selection
        movie_ids = get_all_movie_ids(movies_db)
        if 1 <= choice <= len(movie_ids):
            movie_index = choice - 1
            movie_id = movie_ids[movie_index]
            clear_screen()
            movies_db = _handle_movie_management(movies_db, movie_id)
            return movies_db, True  # Return with changes made