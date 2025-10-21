"""
Core business logic for ticket purchasing operations.
Contains pure business logic without UI concerns.
"""

from custom_types import CinemaHall
from constants.index import SEAT_ICON, BUSY_SEAT_ICON, RESERVED_SEAT_ICON
from tools.seats.index import count_seats, set_seat_status
from tools.seats.input_utils import find_first_free_seats


def get_available_seats_count(hall: CinemaHall) -> int:
    """Gets the number of available seats in a hall."""
    return count_seats(hall)


def validate_ticket_request(available_seats: int, requested_tickets: int) -> tuple[bool, str]:
    """
    Validates if the ticket request is valid.
    Returns (is_valid, error_message)
    """
    if requested_tickets < 1:
        return False, "La cantidad debe ser mayor que 0."
    
    if requested_tickets > available_seats:
        return False, f"No hay suficientes butacas libres. Disponibles: {available_seats}."
    
    return True, ""


def find_consecutive_available_seats(hall: CinemaHall, ticket_count: int) -> list[tuple[int, int]]:
    """Finds consecutive available seats for the requested number of tickets."""
    return find_first_free_seats(hall, ticket_count)


def has_enough_consecutive_seats(found_seats: list, requested_count: int) -> bool:
    """Checks if enough consecutive seats were found."""
    return len(found_seats) >= requested_count


def reserve_seats_temporarily(hall: CinemaHall, seat_positions: list[tuple[int, int]]) -> None:
    """Temporarily reserves seats for preview."""
    for row, col in seat_positions:
        set_seat_status(row, col, hall, RESERVED_SEAT_ICON)


def confirm_seat_purchase(hall: CinemaHall, seat_positions: list[tuple[int, int]]) -> None:
    """Confirms purchase by marking seats as occupied."""
    for row, col in seat_positions:
        set_seat_status(row, col, hall, BUSY_SEAT_ICON)


def cancel_seat_reservation(hall: CinemaHall, seat_positions: list[tuple[int, int]]) -> None:
    """Cancels reservation by making seats available again."""
    for row, col in seat_positions:
        set_seat_status(row, col, hall, SEAT_ICON)


def purchase_individual_seat(hall: CinemaHall, row: int, column: int) -> None:
    """Purchases an individual seat."""
    set_seat_status(row, column, hall, BUSY_SEAT_ICON)