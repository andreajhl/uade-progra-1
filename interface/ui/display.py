

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
        print("\nPelículas disponibles para editar:")
        for i in range(movies_count):
            print(f"{i + 3} - Editar película {i + 1}")
    
    print("9 - Salir\n")


def display_movies_overview(movies_db) -> None:
    """Muestra resumen de todas las películas."""
    from tools.movies.index import get_all_movie_ids, get_movie_by_id
    
    print("Catálogo de Películas:")
    print("\nID \t Título \t\t Categoría \t Clasificación \t Horario")
    print("-" * 80)
    
    movie_ids = get_all_movie_ids(movies_db)
    for i, movie_id in enumerate(movie_ids, 1):
        movie = get_movie_by_id(movies_db, movie_id)
        if movie:
            title = movie["title"][:15] + "..." if len(movie["title"]) > 15 else movie["title"]
            print(f"{i} \t {title:<15} \t {movie['category']} \t\t {movie['classification']} \t\t {movie['schedule']}")
    
    if not movie_ids:
        print("No hay películas disponibles.")
    print()


def display_user_welcome() -> None:
    """Muestra mensaje de bienvenida."""
    print("\tBienvenido.")


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