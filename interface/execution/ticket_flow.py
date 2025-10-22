

from custom_types import CinemaHall, MoviesDatabase
from tools.display.index import clear_screen, show_hall
from tools.movies.index import get_movie_by_id
from interface.core.ticket_operations import (
    validate_ticket_request,
    find_consecutive_available_seats,
    has_enough_consecutive_seats,
    reserve_seats_temporarily,
    confirm_seat_purchase,
    cancel_seat_reservation,
    purchase_individual_seat
)
from interface.ui.display import (
    display_film_name_header,
    display_available_seats_message,
    display_purchase_completion_message,
    display_seat_selection_message,
    display_insufficient_seats_message
)
from interface.ui.input import (
    get_ticket_count_input,
    get_seat_acceptance_choice,
    get_free_seat_selection
)


def run_ticket_purchase_interface(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """Flujo principal de compra de entradas."""
    movie = get_movie_by_id(movies_db, movie_id)
    if not movie:
        print("\n⚠️ Error: Película no encontrada")
        return movies_db
    
    hall = movie["hall"]
    film_name = movie["title"]
    
    available_seats = sum(row.count("L") for row in hall)
    
    if available_seats == 0:
        print("\n🎭 Lo siento, no hay asientos disponibles para esta función")
        return movies_db
        
    clear_screen()
    display_film_name_header(film_name)
    
    ticket_count = get_ticket_count_input(available_seats)
    
    consecutive_seats = find_consecutive_available_seats(hall, ticket_count)
    
    if not has_enough_consecutive_seats(consecutive_seats, ticket_count):
        display_insufficient_seats_message()
        return movies_db
        
    if offer_consecutive_seats(hall, consecutive_seats, ticket_count):
        movies_db[movie_id] = {
            "title": movie["title"],
            "hall": hall,
            "category": movie["category"],
            "classification": movie["classification"],
            "schedule": movie["schedule"]
        }
        return movies_db
        
    handle_individual_seat_selection(hall, ticket_count)
    
    movies_db[movie_id] = {
        "title": movie["title"],
        "hall": hall,
        "category": movie["category"],
        "classification": movie["classification"],
        "schedule": movie["schedule"]
    }
    
    return movies_db


def offer_consecutive_seats(hall: CinemaHall, seat_positions: list[tuple[int, int]], ticket_count: int) -> bool:
    """Ofrece butacas consecutivas al usuario."""
    display_available_seats_message(seat_positions)
    reserve_seats_temporarily(hall, seat_positions)
    show_hall(hall)
    
    choice = get_seat_acceptance_choice()
    
    if choice == 1:
        confirm_seat_purchase(hall, seat_positions)
        display_purchase_completion_message(ticket_count)
        show_hall(hall)
        return True
    else:
        cancel_seat_reservation(hall, seat_positions)
        return False


def handle_individual_seat_selection(hall: CinemaHall, ticket_count: int) -> None:
    """Maneja selección individual de butacas."""
    purchased_count = 0
    
    while purchased_count < ticket_count:
        row, column = get_free_seat_selection(hall)
        purchase_individual_seat(hall, row, column)
        display_seat_selection_message(row, column)
        purchased_count += 1
    
    display_purchase_completion_message(purchased_count)
    show_hall(hall)