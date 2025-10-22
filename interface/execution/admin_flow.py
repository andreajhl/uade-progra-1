

from custom_types import MoviesDatabase
from tools.display.index import clear_screen
from tools.movies.index import (
    get_movies_count,
    add_movie_to_database,
    get_all_movie_ids,
    get_movie_by_id
)
from interface.ui.display import (
    display_admin_menu_header,
    display_admin_menu_options,
    display_movies_overview
)
from interface.ui.input import (
    get_admin_menu_choice_movies,
    get_complete_movie_data
)
from tools.json.index import save_json


def run_admin_interface(movies_db: MoviesDatabase) -> MoviesDatabase:
    """Flujo principal de interfaz de administrador."""
    data_changed = False 
    
    while True:
        show_admin_menu_state(movies_db)
        
        admin_choice = get_admin_menu_choice_movies(get_movies_count(movies_db))
        
        if admin_choice == 1:
            movies_db = handle_create_movie(movies_db)
            data_changed = True
            continue
            
        if admin_choice == 9:
            break
            
        movie_ids = get_all_movie_ids(movies_db)
        if admin_choice > 2 and admin_choice <= len(movie_ids) + 2:
            movie_index = admin_choice - 3 
            if movie_index < len(movie_ids):
                clear_screen()
                movie_id = movie_ids[movie_index]
                movies_db = handle_movie_management(movies_db, movie_id)
                data_changed = True

    if data_changed:
        save_json(movies_db)
    
    clear_screen()
    return movies_db


def show_admin_menu_state(movies_db: MoviesDatabase) -> None:
    """Muestra el estado del menú de administrador."""
    display_admin_menu_header()
    display_movies_overview(movies_db)
    display_admin_menu_options(get_movies_count(movies_db))


def handle_create_movie(movies_db: MoviesDatabase) -> MoviesDatabase:
    """Maneja la creación de una nueva película."""
    movie_data = get_complete_movie_data()
    
    from interface.core.hall_operations import create_new_hall
    new_hall = create_new_hall()
    
    movies_db, movie_id = add_movie_to_database(
        movies_db,
        title=movie_data["title"],
        hall=new_hall,
        category=movie_data["category"],
        classification=movie_data["classification"], 
        schedule=movie_data["schedule"]
    )
    
    print(f"\n✅ Película creada exitosamente: '{movie_data['title']}'")
    print(f"🎭 Categoría: {movie_data['category']}")
    print(f"🔞 Clasificación: {movie_data['classification']}")
    print(f"📅 Horario: {movie_data['schedule']}")
    print(f"🆔 ID: {movie_id}")
    
    input("\n📌 Presione Enter para continuar...")
    clear_screen()
    return movies_db


def handle_movie_management(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """Maneja edición de película específica."""
    movie = get_movie_by_id(movies_db, movie_id)
    if not movie:
        print(f"❌ Película con ID {movie_id} no encontrada")
        return movies_db
    
    from interface.execution.hall_admin_flow import run_hall_admin_interface
    return run_hall_admin_interface(movies_db, movie_id)