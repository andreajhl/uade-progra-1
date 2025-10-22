

from custom_types import CinemaHall
from constants.index import SEAT_ICON, BUSY_SEAT_ICON, RESERVED_SEAT_ICON
from tools.seats.index import count_seats, set_seat_status, get_first_free_seats


def get_available_seats_count(hall: CinemaHall) -> int:
    """Obtiene número de butacas disponibles."""
    return count_seats(hall)


def validate_ticket_request(available_seats: int, requested_tickets: int) -> tuple[bool, str]:
    """Valida si la solicitud de entradas es válida."""
    if requested_tickets < 1:
        return False, "La cantidad debe ser mayor que 0."
    
    if requested_tickets > available_seats:
        return False, f"No hay suficientes butacas libres. Disponibles: {available_seats}."
    
    return True, ""


def find_consecutive_available_seats(hall: CinemaHall, ticket_count: int) -> list[tuple[int, int]]:
    """Encuentra butacas consecutivas disponibles."""
    return get_first_free_seats(hall, ticket_count)


def has_enough_consecutive_seats(found_seats: list, requested_count: int) -> bool:
    """Verifica si se encontraron suficientes butacas consecutivas."""
    return len(found_seats) >= requested_count


def reserve_seats_temporarily(hall: CinemaHall, seat_positions: list[tuple[int, int]]) -> None:
    """Reserva temporalmente butacas para vista previa."""
    for row, col in seat_positions:
        set_seat_status(row, col, hall, RESERVED_SEAT_ICON)


def confirm_seat_purchase(hall: CinemaHall, seat_positions: list[tuple[int, int]]) -> None:
    """Confirma compra marcando butacas como ocupadas."""
    for row, col in seat_positions:
        set_seat_status(row, col, hall, BUSY_SEAT_ICON)


def cancel_seat_reservation(hall: CinemaHall, seat_positions: list[tuple[int, int]]) -> None:
    """Cancela reserva haciendo butacas disponibles nuevamente."""
    for row, col in seat_positions:
        set_seat_status(row, col, hall, SEAT_ICON)


def purchase_individual_seat(hall: CinemaHall, row: int, column: int) -> None:
    """Compra butaca individual."""
    set_seat_status(row, column, hall, BUSY_SEAT_ICON)