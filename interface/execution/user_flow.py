from custom_types import MoviesDatabase
from tools.display.index import clear_screen
from constants.index import FILM_CATEGORY
from tools.movies.index import (
    get_movie_by_id,
    search_movies_by_name,
    search_movies_by_category,
    get_all_movies_list,
)
from interface.ui.display import (
    display_user_welcome,
    display_user_menu_options,
    display_filtered_movies,
)
from interface.ui.input import (
    get_user_main_menu_choice,
    get_movie_name_search,
    get_category_choice,
    get_filtered_movie_choice,
)
from tools.json.index import save_json
from interface.execution.ticket_flow import run_ticket_purchase_interface


def run_user_interface(movies_db: MoviesDatabase) -> MoviesDatabase:
    """Flujo principal de interfaz de usuario."""
    data_changed = False

    while True:
        show_user_menu_state(movies_db)

        user_choice = get_user_main_menu_choice()

        if user_choice == 9:
            break

        if user_choice == 1:
            movies_db = handle_view_all_movies(movies_db)
            data_changed = True
        elif user_choice == 2:
            movies_db = handle_search_by_name(movies_db)
            data_changed = True
        elif user_choice == 3:
            movies_db = handle_search_by_category(movies_db)
            data_changed = True

        clear_screen()

    if data_changed:
        save_json(movies_db)

    clear_screen()
    return movies_db


def show_user_menu_state(movies_db: MoviesDatabase) -> None:
    """Muestra el estado del menú de usuario."""
    display_user_welcome()
    display_user_menu_options()


def handle_view_all_movies(movies_db: MoviesDatabase) -> MoviesDatabase:
    """Maneja la visualización de todas las películas y permite la selección de películas."""
    all_movies = get_all_movies_list(movies_db)

    if not all_movies:
        print("📽️ No hay películas disponibles en este momento.")
        input("Presiona Enter para continuar...")
        return movies_db

    display_filtered_movies(all_movies, "Todas las películas disponibles")

    movie_choice = get_filtered_movie_choice(len(all_movies))

    if movie_choice == 9:
        return movies_db

    if movie_choice > 0 and movie_choice <= len(all_movies):
        movie_id, _ = all_movies[movie_choice - 1]
        return handle_movie_selection(movies_db, movie_id)

    return movies_db


def handle_search_by_name(movies_db: MoviesDatabase) -> MoviesDatabase:
    """Maneja la búsqueda de películas por nombre."""
    search_term = get_movie_name_search()

    if not search_term.strip():
        return movies_db

    matching_movies = search_movies_by_name(movies_db, search_term)

    if not matching_movies:
        print(f"🔍 No se encontraron películas con el nombre '{search_term}'")
        input("Presiona Enter para continuar...")
        return movies_db

    display_filtered_movies(
        matching_movies, f"Películas encontradas para '{search_term}'"
    )

    movie_choice = get_filtered_movie_choice(len(matching_movies))

    if movie_choice == 9:
        return movies_db

    if movie_choice > 0 and movie_choice <= len(matching_movies):
        movie_id, _ = matching_movies[movie_choice - 1]
        return handle_movie_selection(movies_db, movie_id)

    return movies_db


def handle_search_by_category(movies_db: MoviesDatabase) -> MoviesDatabase:
    """Maneja la búsqueda de películas por categoría."""
    all_movies = get_all_movies_list(movies_db)
    category_ids = list(set(movie["category"] for movie_id, movie in all_movies))
    category_ids.sort()

    if not category_ids:
        print("📽️ No hay categorías disponibles.")
        input("Presiona Enter para continuar...")
        return movies_db

    category_descriptions = [FILM_CATEGORY[cat_id] for cat_id in category_ids]

    selected_description = get_category_choice(category_descriptions)

    selected_category_id = None
    for cat_id, description in FILM_CATEGORY.items():
        if description == selected_description:
            selected_category_id = cat_id
            break

    if not selected_category_id:
        return movies_db

    matching_movies = search_movies_by_category(movies_db, selected_category_id)

    if not matching_movies:
        print(
            f"🎭 No se encontraron películas en la categoría '{selected_description}'"
        )
        input("Presiona Enter para continuar...")
        return movies_db

    display_filtered_movies(matching_movies, f"Películas de '{selected_description}'")

    movie_choice = get_filtered_movie_choice(len(matching_movies))

    if movie_choice == 9:
        return movies_db

    if movie_choice > 0 and movie_choice <= len(matching_movies):
        movie_id, _ = matching_movies[movie_choice - 1]
        return handle_movie_selection(movies_db, movie_id)

    return movies_db


def handle_movie_selection(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """Maneja selección de película para compra de entradas."""
    movie = get_movie_by_id(movies_db, movie_id)
    if not movie:
        print(f"❌ Película con ID {movie_id} no encontrada")
        return movies_db

    return run_ticket_purchase_interface(movies_db, movie_id)
