
from interface.execution.admin_flow import get_category, get_classification
from custom_types import CinemaHall
from tools.display.index import show_hall

def display_admin_menu_header() -> None:
    """Muestra encabezado del panel de administrador."""
    print("\tPanel de administración.")


def display_admin_menu_options(movies_count: int) -> None:
    """Muestra opciones del menú de administrador."""
    print(f"""
películas totales: {movies_count}

1 - Agregar función de cine""")
    
    if movies_count > 0:
        print("2 - Editar película")
    
    print("9 - Salir\n")


def display_movie_selection_menu(movies_db) -> None:
    """Muestra el menú de selección de películas para editar."""
    from tools.movies.index import get_all_movie_ids, get_movie_by_id
    
    print("\n" + "="*50)
    print("         SELECCIONAR PELÍCULA PARA EDITAR")
    print("="*50)
    
    movie_ids = get_all_movie_ids(movies_db)
    for i, movie_id in enumerate(movie_ids, 1):
        movie = get_movie_by_id(movies_db, movie_id)
        if movie:
            title = movie["title"][:30] + "..." if len(movie["title"]) > 30 else movie["title"]
            categories = get_category()
            category=categories[movie["category"]]
            classifications = get_classification()
            classification = classifications[movie["classification"]]
            
            print(f"{i} - {title} ({category}, {classification})")
    
    print("9 - Volver al menú anterior")
    print("="*50)


def display_movies_overview(movies_db) -> None:
    """Muestra resumen de todas las películas."""
    from tools.movies.index import get_all_movie_ids, get_movie_by_id
    
    print("Catálogo de Películas:")
    print("\nID \t Título \t\t Categoría \t\t\t Clasificación \t\t\t\t Horario")
    print("-" * 120)
    
    movie_ids = get_all_movie_ids(movies_db)
    for i, movie_id in enumerate(movie_ids, 1):
        movie = get_movie_by_id(movies_db, movie_id)
        if movie:
            title = movie["title"][:15] + "..." if len(movie["title"]) > 15 else movie["title"]
            categories = get_category()
            category=categories[movie["category"]]
            classifications = get_classification()
            classification = classifications[movie["classification"]]

            print(f"{i} \t {title:<15} \t {category} \t\t {classification} \t\t {movie['schedule']}")
    
    if not movie_ids:
        print("No hay películas disponibles.")
    print()


def display_user_welcome() -> None:
    """Muestra mensaje de bienvenida."""
    print("\tBienvenido.")


def display_user_menu_options() -> None:
    """Muestra las opciones del menú del usuario."""
    print("""
1 - Ver listado de películas
2 - Buscar película por nombre
3 - Buscar película por categoría
9 - Salir
""")


def display_filtered_movies(movies_list: list, title: str) -> None:
    """Muestra la lista de películas filtradas."""
    print(f"\n{title}")
    print("="*50)
    
    if not movies_list:
        print("No se encontraron películas que coincidan con la busqueda.")
        print("="*50)
        return
    
    for i, (_, movie) in enumerate(movies_list, 1):
        title = movie['title']
        categories = get_category()
        category=categories[movie["category"]]
        classifications = get_classification()
        classification = classifications[movie["classification"]]

        print(f"{i} - Título: {title}")
        print(f"    Categoría: {category}")
        print(f"    Clasificación: {classification}")
        print(f"    Horario: {movie['schedule']}")
        print()
    
    print("9 - Volver al menú anterior")
    print("="*50)


def display_hall_admin_header(film_name: str) -> None:
    """Muestra encabezado de administración de sala."""
    print("\tPanel de administración.")
    print(film_name)


def display_hall_details(hall: CinemaHall) -> None:
    """Muestra diseño de la sala."""
    show_hall(hall)
    print()


def display_hall_admin_options() -> None:
    """Muestra opciones de administración de sala."""
    print("""1 - marcar como Ocupada/Deshabilitada/Habilitada una butaca
2 - Cambiar nombre de pelicula
3 - Limpiar todos los asientos ocupados
4 - Eliminar sala
9 - Guardar y salir\n""")


def display_seat_status_options() -> None:
    """Muestra opciones para cambiar estado de butaca."""
    print("Marcar como:")
    print("""1 - Habilitada\n2 - Ocupada\n3 - Deshabilitada\n""")


def display_film_name_header(film_name: str) -> None:
    """Muestra nombre de película."""
    print(film_name)


def display_available_seats_message(seat_positions: list[tuple[int, int]]) -> None:
    """Muestra mensaje sobre butacas disponibles."""
    print("Las siguientes butacas están disponibles para usted:")


def display_purchase_completion_message(ticket_count: int) -> None:
    """Muestra mensaje de compra completada."""
    print(f"Compra finalizada. Entradas adquiridas: {ticket_count}.")


def display_seat_selection_message(row: int, column: int) -> None:
    """Muestra información de butaca seleccionada."""
    print(f"Seleccionaste la butaca F{row+1}-C{column+1}.")


def display_insufficient_seats_message() -> None:
    """Muestra mensaje cuando no hay suficientes butacas."""
    print("No hay suficientes butacas libres.")