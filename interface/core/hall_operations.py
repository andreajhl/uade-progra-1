"""
Core business logic for hall management operations.
Contains pure business logic without UI concerns.
"""

from custom_types import CinemaHall
from constants.index import SEAT_ICON, BUSY_SEAT_ICON, DISABLED_SEAT_ICON
from tools.halls.index import create_halls
from tools.seats.index import get_seat_status, set_seat_status


def create_new_hall() -> CinemaHall:
    """Creates a new cinema hall."""
    from tools.input.index import custom_input
    from tools.display.index import show_hall
    from tools.seats.index import get_coords_seat
    
    # Get hall dimensions
    rows: int = custom_input(
        "Ingresa el numero de filas que tendra la sala: ",
        int,
        validator=lambda rows: (None, rows) if rows >= 1 else ("Minimo 1 fila", None),
    )

    columns: int = custom_input(
        "Ingresa el numero de columnas que tendra la sala: ",
        int,
        validator=lambda columns: (
            (None, columns) if columns >= 1 else ("Minimo 1 columna", None)
        ),
    )

    print()
    hall = create_halls(rows, columns)

    # Disable seats workflow
    option = None
    while option != 2:
        show_hall(hall)
        option: int = custom_input(
            input_message="¿Desea inhabilitar alguna butaca? (1=Sí, 2=No): ",
            input_type=int,
            validator=lambda inpt: (
                (None, inpt)
                if 1 == inpt or inpt == 2
                else ("Opción inválida. Ingrese 1 o 2.", None)
            ),
        )

        if option == 2:
            print("Finalizó la inhabilitación de butacas.")
            break

        row, column = get_coords_seat(hall)
        print()
        row_label = row + 1
        col_label = column + 1

        seat_status = get_seat_status(hall[row][column])

        if seat_status is None:
            print(
                f"La butaca {row_label}{col_label} ya está inhabilitada.", end="\n" * 2
            )
            continue

        if seat_status is False:
            print(
                f"No se puede inhabilitar: la butaca F{row_label}-C{col_label} está ocupada.",
                end="\n" * 2,
            )
            continue

        set_seat_status(row, column, hall, DISABLED_SEAT_ICON)
        print(
            f"Butaca F{row_label}-C{col_label} inhabilitada correctamente.",
            end="\n" * 2,
        )

    return hall


def add_hall_to_complex(all_halls: list[CinemaHall], all_films_names: list[str], film_name: str) -> tuple[list[CinemaHall], list[str]]:
    """Adds a new hall with its film to the cinema complex."""
    new_hall = create_new_hall()
    all_halls.append(new_hall)
    all_films_names.append(film_name)
    return all_halls, all_films_names


def change_seat_status(hall: CinemaHall, row: int, column: int, status_option: int) -> None:
    """
    Changes the status of a specific seat.
    status_option: 1=Available, 2=Occupied, 3=Disabled
    """
    if status_option == 1:
        hall[row][column] = SEAT_ICON
    elif status_option == 2:
        hall[row][column] = BUSY_SEAT_ICON
    else:
        hall[row][column] = DISABLED_SEAT_ICON


def clear_all_occupied_seats(hall: CinemaHall) -> None:
    """Clears all occupied seats in the hall."""
    for row_id in range(len(hall)):
        for col_id in range(len(hall[row_id])):
            if hall[row_id][col_id] == BUSY_SEAT_ICON:
                hall[row_id][col_id] = SEAT_ICON


def remove_hall_from_complex(all_halls: list[CinemaHall], all_films_names: list[str], hall_id: int) -> tuple[list[CinemaHall], list[str]]:
    """Removes a hall from the cinema complex."""
    all_halls.pop(hall_id)
    all_films_names.pop(hall_id)
    return all_halls, all_films_names


def update_film_name(all_films_names: list[str], hall_id: int, new_name: str) -> None:
    """Updates the film name for a specific hall."""
    all_films_names[hall_id] = new_name


def get_hall_count(all_halls: list) -> int:
    """Gets the total number of halls."""
    return len(all_halls)


def get_hall_indexes(all_halls: list) -> range:
    """Gets valid hall indexes range."""
    return range(len(all_halls))


def is_valid_hall_index(all_halls: list, index: int) -> bool:
    """Checks if a hall index is valid."""
    return index in range(len(all_halls))