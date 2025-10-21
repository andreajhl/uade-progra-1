"""
UI input functions for getting user input.
Contains only input logic with validation.
"""

from tools.input.index import custom_input
from tools.seats.index import get_coords_seat, get_free_seat
from custom_types import CinemaHall


def get_admin_menu_choice_movies(movies_count: int) -> int:
    """Gets admin menu choice for movies system with validation."""
    valid_options = [1, 9]  # 1=Create movie, 9=Exit
    
    if movies_count > 0:
        valid_options.append(2)  # 2=Edit movie (shows submenu)
    
    return custom_input(
        "Elija una opción: ",
        int,
        error_message="Opción inválida.",
        validator=lambda option: (
            ("Opción inválida.", None)
            if option not in valid_options
            else (None, option)
        ),
    )


def get_movie_selection_choice(movies_count: int) -> int:
    """Gets movie selection choice for editing with validation."""
    valid_options = [9]  # 9=Back
    if movies_count > 0:
        valid_options.extend(range(1, movies_count + 1))  # Movie selection options
    
    return custom_input(
        "Seleccione una película: ",
        int,
        error_message="Opción inválida.",
        validator=lambda option: (
            ("Opción inválida.", None)
            if option not in valid_options
            else (None, option)
        ),
    )


def get_admin_menu_choice(halls_count: int) -> int:
    """Gets admin menu choice with validation."""
    halls_indexes = range(halls_count)
    
    return custom_input(
        "Elija una sala: ",
        int,
        error_message="Opcion invalida.",
        validator=lambda option: (
            ("Opcion invalida.", None)
            if not ((option - 1) in halls_indexes) and not (option in (1, 2, 9))
            else (None, option)
        ),
    )


def get_user_menu_choice_movies(movies_count: int) -> int:
    """Gets user menu choice for movies system with validation."""
    valid_options = [9]  # 9=Admin mode
    if movies_count > 0:
        valid_options.extend(range(1, movies_count + 1))  # Movie selection options
    
    return custom_input(
        "Elija una película (9 para entrar en modo administrador): ",
        int,
        error_message="Opción inválida.",
        validator=lambda option: (
            ("Opción inválida.", None)
            if option not in valid_options
            else (None, option)
        ),
    )


def get_user_menu_choice(halls_count: int) -> int:
    """Gets user menu choice with validation."""
    halls_indexes = range(halls_count)
    
    return custom_input(
        "Elija una sala (9 para entrar en modo administrador): ",
        int,
        error_message="Opcion invalida.",
        validator=lambda option: (
            ("Opcion invalida.", None)
            if not (option - 1 in halls_indexes) and option != 9
            else (None, option)
        ),
    )


def get_hall_admin_choice() -> int:
    """Gets hall administration menu choice."""
    options_tuple = (1, 2, 3, 4, 9)
    return custom_input(
        "opcion: ",
        int,
        error_message="Opcion invalida.",
        validator=lambda option: (
            ("Opcion invalida.", None)
            if not (option in options_tuple)
            else (None, option)
        ),
    )


def get_seat_status_choice() -> int:
    """Gets seat status change choice."""
    return custom_input(
        "opcion: ",
        int,
        error_message="Opcion invalida.",
        validator=lambda option: (
            ("Opcion invalida.", None)
            if not (option in (1, 2, 3))
            else (None, option)
        ),
    )


def get_film_name_input() -> str:
    """Gets film name input."""
    return custom_input("Título de la película: ", str)


def get_new_film_name_input() -> str:
    """Gets new film name input."""
    return input("En esta sala se proyectará: ")


def get_movie_category_input() -> str:
    """Gets movie category input with validation."""
    print("\nCategorías disponibles:")
    print("A - Éxito de taquilla")
    print("B - Drama/Romance") 
    print("C - Acción/Aventura")
    print("D - Terror/Suspenso")
    
    return custom_input(
        "Seleccione la categoría (A/B/C/D): ",
        str,
        validator=lambda category: (
            (None, category.upper())
            if category.upper() in ["A", "B", "C", "D"]
            else ("Categoría inválida. Debe ser A, B, C o D.", None)
        ),
    )


def get_movie_classification_input() -> str:
    """Gets movie age classification input with validation."""
    print("\nClasificaciones disponibles:")
    print("ATP - Apta para todo público")
    print("+13 - Mayores de 13 años")
    print("+16 - Mayores de 16 años") 
    print("+18 - Mayores de 18 años")
    
    return custom_input(
        "Seleccione la clasificación (ATP/+13/+16/+18): ",
        str,
        validator=lambda classification: (
            (None, classification.upper() if classification.upper() == "ATP" else classification)
            if classification.upper() in ["ATP"] or classification in ["+13", "+16", "+18"]
            else ("Clasificación inválida. Debe ser ATP, +13, +16 o +18.", None)
        ),
    )


def get_movie_schedule_input() -> str:
    """Gets movie schedule input with basic date validation."""
    print("\nIngrese el horario de función")
    
    return custom_input(
        "Fecha (formato DD/MM/AAAA): ",
        str,
        validator=lambda date_str: _validate_date_input(date_str)
    )


def _validate_date_input(date_str: str) -> tuple[str | None, str | None]:
    """Validates date format for schedule input."""
    try:
        parts = date_str.split('/')
        if len(parts) != 3:
            return ("Formato incorrecto. Use DD/MM/AAAA", None)
        
        day, month, year = map(int, parts)
        
        # Basic validation
        if not (1 <= day <= 31):
            return ("Día debe estar entre 1 y 31", None)
        if not (1 <= month <= 12):
            return ("Mes debe estar entre 1 y 12", None)
        if not (1900 <= year <= 2100):
            return ("Año debe estar entre 1900 y 2100", None)
            
        # Format with leading zeros
        formatted_date = f"{day:02d}/{month:02d}/{year}"
        return (None, formatted_date)
        
    except ValueError:
        return ("Formato incorrecto. Use números en formato DD/MM/AAAA", None)


def get_ticket_count_input(available_seats: int) -> int:
    """Gets ticket count with validation."""
    return custom_input(
        f"Ingrese el número de entradas a comprar (disponibles: {available_seats}): ",
        int,
        validator=lambda requested: (
            ("La cantidad debe ser mayor que 0.", None)
            if requested < 1
            else (
                (f"No hay suficientes butacas libres. Disponibles: {available_seats}.", None)
                if requested > available_seats
                else (None, requested)
            )
        ),
    )


def get_seat_acceptance_choice() -> int:
    """Gets choice for accepting suggested seats."""
    return custom_input(
        "¿Desea aceptar estas butacas? (1 = si/ 2 = no): ",
        int,
        validator=lambda x: (
            (None, x) if x in [1, 2] else ("Ingrese '1 = Sí', '2 = No'.", None)
        ),
    )


def get_seat_coordinates(hall: CinemaHall) -> tuple[int, int]:
    """Gets seat coordinates input."""
    return get_coords_seat(hall)


def get_free_seat_selection(hall: CinemaHall) -> tuple[int, int]:
    """Gets free seat selection input."""
    return get_free_seat(hall)


def get_complete_movie_data() -> dict[str, str]:
    """
    Gets complete movie data including title, category, classification, and schedule.
    Returns a dictionary with all movie information.
    """
    print("\n" + "="*50)
    print("         INFORMACIÓN DE LA PELÍCULA")
    print("="*50)
    
    # Get movie title
    title = get_film_name_input()
    
    # Get movie category
    category = get_movie_category_input()
    
    # Get age classification  
    classification = get_movie_classification_input()
    
    # Get schedule
    schedule = get_movie_schedule_input()
    
    print("\n✅ Información de película completada")
    print(f"📽️  Título: {title}")
    print(f"🎭 Categoría: {category}")
    print(f"🔞 Clasificación: {classification}")
    print(f"📅 Horario: {schedule}")
    
    return {
        "title": title,
        "category": category,
        "classification": classification,
        "schedule": schedule
    }