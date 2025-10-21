"""
Execution flow for hall administration operations.
Coordinates between UI input/display and core business logic.
"""

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


def run_hall_admin_interface(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """
    Main execution flow for hall administration.
    Broken down from original all-powerful function.
    """
    data_changed = False  # Flag to track if any changes were made
    
    while True:
        movie = get_movie_by_id(movies_db, movie_id)
        if not movie:
            print(f"❌ Película con ID {movie_id} no encontrada")
            break
            
        hall = movie["hall"]
        film_name = movie["title"]
        
        # Display hall admin state
        _show_hall_admin_state(hall, film_name)
        
        # Get admin choice
        admin_choice = get_hall_admin_choice()
        
        # Handle different operations
        if admin_choice == 1:
            _handle_seat_status_change(hall)
            # Update the movie in the database with modified hall
            movies_db[movie_id] = {
                "title": movie["title"],
                "hall": hall,
                "category": movie["category"],
                "classification": movie["classification"],
                "schedule": movie["schedule"]
            }
            data_changed = True
        elif admin_choice == 2:
            movies_db = _handle_film_name_change(movies_db, movie_id)
            data_changed = True
        elif admin_choice == 3:
            _handle_clear_occupied_seats(hall)
            # Update the movie in the database with modified hall
            movies_db[movie_id] = {
                "title": movie["title"],
                "hall": hall,
                "category": movie["category"],
                "classification": movie["classification"],
                "schedule": movie["schedule"]
            }
            data_changed = True
        elif admin_choice == 4:
            # Delete the movie from the database
            movies_db = delete_movie(movies_db, movie_id)
            print(f"\n🗑️ Película '{film_name}' eliminada exitosamente")
            data_changed = True
            input("\n📌 Presione Enter para continuar...")
            break
        elif admin_choice == 9:
            break
            
        clear_screen()
    
    # Save data only if changes were made
    if data_changed:
        save_json(movies_db)
    
    return movies_db


def _show_hall_admin_state(hall: CinemaHall, film_name: str) -> None:
    """Shows the current hall admin state."""
    display_hall_admin_header(film_name)
    display_hall_details(hall)
    display_hall_admin_options()


def _handle_seat_status_change(hall: CinemaHall) -> None:
    """Handles changing the status of a seat."""
    row, column = get_seat_coordinates(hall)
    display_seat_status_options()
    status_choice = get_seat_status_choice()
    change_seat_status(hall, row, column, status_choice)


def _handle_film_name_change(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """Handles changing the film name for a movie."""
    new_name = get_new_film_name_input()
    
    movie = get_movie_by_id(movies_db, movie_id)
    if movie:
        # Update the movie with the new title
        movies_db[movie_id] = {
            "title": new_name,
            "hall": movie["hall"],
            "category": movie["category"],
            "classification": movie["classification"],
            "schedule": movie["schedule"]
        }
        print(f"\n✅ Título de película actualizado a: '{new_name}'")
    
    return movies_db


def _handle_clear_occupied_seats(hall: CinemaHall) -> None:
    """Handles clearing all occupied seats in the hall."""
    clear_all_occupied_seats(hall)