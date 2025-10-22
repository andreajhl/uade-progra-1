

from tools.input.index import custom_input
from tools.seats.index import get_coords_seat, get_free_seat
from custom_types import CinemaHall


def get_admin_menu_choice_movies(movies_count: int) -> int:
    """Obtiene opción del menú de administrador."""
    valid_options = [1, 2, 9]
    if movies_count > 0:
        valid_options.extend(range(3, movies_count + 3))
    
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


def get_admin_menu_choice(halls_count: int) -> int:
    """Obtiene opción del menú de administrador."""
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
    """Obtiene opción del menú de usuario."""
    valid_options = [9]
    if movies_count > 0:
        valid_options.extend(range(1, movies_count + 1))
    
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
    """Obtiene opción del menú de usuario."""
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
    """Obtiene opción de administración de sala."""
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
    """Obtiene opción de cambio de estado de butaca."""
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
    """Obtiene nombre de película."""
    return custom_input("Título de la película: ", str)


def get_new_film_name_input() -> str:
    """Obtiene nuevo nombre de película."""
    return input("En esta sala se proyectará: ")


def get_movie_category_input() -> str:
    """Obtiene categoría de película."""
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
    """Obtiene clasificación de edad de película."""
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
    """Obtiene horario de película."""
    print("\nIngrese el horario de función")
    
    return custom_input(
        "Fecha (formato DD/MM/AAAA): ",
        str,
        validator=lambda date_str: validate_date_input(date_str)
    )


def validate_date_input(date_str: str) -> tuple[str | None, str | None]:
    """Valida formato de fecha."""
    try:
        parts = date_str.split('/')
        if len(parts) != 3:
            return ("Formato incorrecto. Use DD/MM/AAAA", None)
        
        day, month, year = map(int, parts)
        
        if not (1 <= day <= 31):
            return ("Día debe estar entre 1 y 31", None)
        if not (1 <= month <= 12):
            return ("Mes debe estar entre 1 y 12", None)
        if not (1900 <= year <= 2100):
            return ("Año debe estar entre 1900 y 2100", None)
            
        formatted_date = f"{day:02d}/{month:02d}/{year}"
        return (None, formatted_date)
        
    except ValueError:
        return ("Formato incorrecto. Use números en formato DD/MM/AAAA", None)


def get_ticket_count_input(available_seats: int) -> int:
    """Obtiene cantidad de entradas."""
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
    """Obtiene opción de aceptar butacas sugeridas."""
    return custom_input(
        "¿Desea aceptar estas butacas? (1 = si/ 2 = no): ",
        int,
        validator=lambda x: (
            (None, x) if x in [1, 2] else ("Ingrese '1 = Sí', '2 = No'.", None)
        ),
    )


def get_seat_coordinates(hall: CinemaHall) -> tuple[int, int]:
    """Obtiene coordenadas de butaca."""
    return get_coords_seat(hall)


def get_free_seat_selection(hall: CinemaHall) -> tuple[int, int]:
    """Obtiene selección de butaca libre."""
    return get_free_seat(hall)


def get_complete_movie_data() -> dict[str, str]:
    """Obtiene datos completos de película."""
    print("\n" + "="*50)
    print("         INFORMACIÓN DE LA PELÍCULA")
    print("="*50)
    
    title = get_film_name_input()
    
    category = get_movie_category_input()
    
    classification = get_movie_classification_input()
    
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