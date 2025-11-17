
from tools.input.index import custom_input
from tools.seats.index import get_coords_seat, get_free_seat
from custom_types import CinemaHall
from tools.movies.index import get_categories, get_classifications
from constants.index import CONST_MESES

def get_admin_menu_choice_movies(movies_count: int) -> int:
    """Obtiene opción del menú de administrador."""
    valid_options = [1,3,4,9]
    if movies_count > 0:
        valid_options.append(2)
        print(valid_options)
    
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
    """Obtiene la opción de selección de películas para editar y valida la opción."""
    valid_options = [9] 
    if movies_count > 0:
        valid_options.extend(range(1, movies_count + 1)) 
    
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
    """Gets user menu choice for movies system with validation."""
    valid_options = [9]  # 9=Exit to main menu
    if movies_count > 0:
        valid_options.extend(range(1, movies_count + 1))
    
    return custom_input(
        "Elija una película (9 para salir): ",
        int,
        error_message="Opción inválida.",
        validator=lambda option: (
            ("Opción inválida.", None)
            if option not in valid_options
            else (None, option)
        ),
    )


def get_user_main_menu_choice() -> int:
    """Gets user main menu choice with validation."""
    valid_options = [1, 2, 3, 9]
    
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


def get_movie_name_search() -> str:
    """Gets movie name for search."""
    return custom_input(
        "Ingrese el nombre de la película a buscar: ",
        str,
        validator=lambda name: (
            ("El nombre no puede estar vacío.", None)
            if not name.strip()
            else (None, name.strip())
        )
    )


def get_category_choice(categories: list[str]) -> str:
    """Gets category choice for search."""
    print("\nCategorías disponibles:")
    for i, category in enumerate(categories, 1):
        print(f"{i} - {category}")
    
    choice = custom_input(
        f"Seleccione la categoría (1-{len(categories)}): ",
        int,
        validator=lambda num: (
            (None, num)
            if 1 <= num <= len(categories)
            else (f"Categoría inválida. Debe ser entre 1 y {len(categories)}.", None)
        ),
    )
    
    return categories[choice - 1]  # Return the selected category name


def get_filtered_movie_choice(movies_count: int) -> int:
    """Gets choice from filtered movie list."""
    valid_options = [9]  # 9=Back
    if movies_count > 0:
        valid_options.extend(range(1, movies_count + 1))
    
    return custom_input(
        "Seleccione una película para comprar entradas: ",
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
        "Elija una sala (9 para salir): ",
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
    categories = get_categories()
    qty_categories = len(categories)

    for key, category in categories.items():
        print(f"{key}. {category}")

    return custom_input(
        f"Seleccione la categoría (1-{qty_categories}): ",
        str,
        validator=lambda category: (
            (None, category)
            if category in categories.keys()
            else (f"Categoría inválida. Debe estar entre 1 y {qty_categories}", None)
        ),
    )
    
def get_movie_classification_input() -> str:
    """Obtiene clasificación de edad de película."""
    print("\nClasificaciones disponibles:")
    classifications = get_classifications()
    qty_classifications = len(classifications)

    for key, value in classifications.items():
        print(f"{key}. {value}")

    return custom_input(
        f"Seleccione la clasificación (1-{qty_classifications}): ",
        str,
        validator=lambda c: (
            (None, c)
            if c in classifications.keys()
            else (f"Clasificación inválida. Debe estar entre 1 y {qty_classifications}", None)
        ),
    )



def get_movie_schedule_input() -> str:
    """Obtiene Fecha de película."""
    print("\nIngrese la fecha de la función")
    
    return custom_input(
        "Fecha (formato DD/MM/AAAA): ",
        str,
        validator=lambda date_str: validate_date_input(date_str)
    )


def split_date(date):
    """Separa componenetes de la fecha"""
    day=int(date[:2])
    if int(date[3])==0:
        month=int(date[4:5])
    else:
        month=int(date[3:5])        
    year=int(date[6:10])

    return(day, month, year)

def valid_day(day,mont_comp):
    """Valida que el dia este """
    meses= CONST_MESES
    return(0<int(day)<=meses.get((int(mont_comp))))

def validate_date_input(date_str: str) -> tuple[str | None, str | None]:
    """Valida formato de fecha."""
    try:
        parts = date_str.split('/')
        if len(parts) != 3:
            return ("Formato incorrecto. Use DD/MM/AAAA", None)
        
        day, month, year = split_date(date_str)
        
        if not (1 <= month <= 12):
            return ("Mes debe estar entre 1 y 12", None)
        if not (1900 <= year <= 2100):
            return ("Año debe estar entre 1900 y 2100", None)
        if not valid_day(day,month):
            return ("Día Invalido para el mes indicado", None)
            
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


def get_complete_movie_data() -> dict:
    """Obtiene datos completos de película."""
    print("\n" + "="*50)
    print("         INFORMACIÓN DE LA PELÍCULA")
    print("="*50)

    title = get_film_name_input()
    categories = get_categories()
    category = get_movie_category_input()

    classifications = get_classifications()
    classification = get_movie_classification_input()

    schedule = get_movie_schedule_input()

    print("\n✅ Información de película completada")
    print(f"📽️  Título: {title}")
    print(f"🎭 Categoría: {categories[category]}")
    print(f"🔞 Clasificación: {classifications[classification]}")
    print(f"📅 Fecha: {schedule}")

    return {
        "title": title,
        "category": category,
        "classification": classification,
        "schedule": schedule
    }
