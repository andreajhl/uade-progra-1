from constants.index import (MOVIE_PATH, CATEGORY_PATH, CLASSIFICATION_PATH, DEFAULT_CATEGORY, DEFAULT_CLASSIFICATION)
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
    display_movies_overview,
    display_movie_selection_menu
)
from interface.ui.input import (
    get_admin_menu_choice_movies,
    get_complete_movie_data,
    get_movie_selection_choice
)
from tools.json.index import (save_json, read_json)
from tools.movies.index import get_categories, get_classifications
from tools.input.index import custom_input

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
            
        elif admin_choice == 2:
            result = handle_edit_movie_selection(movies_db)
            if result is not None:
                movies_db, changed = result
                if changed:
                    data_changed = True
            continue
        
        elif admin_choice == 3:
            result=edit_classifications()
            if result is not None:
                data_changed = True
            continue
        
        elif admin_choice == 4:
            result=edit_category()
            if result is not None:
                data_changed = True
            continue
                            
        elif admin_choice == 9:
            break

    if data_changed:
        save_json(movies_db,MOVIE_PATH)
    
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
    
    categories=get_categories()
    classifications=get_classifications()
    title=movie_data["title"]
    category=(movie_data["category"])
    classification=(movie_data["classification"])
    schedule=movie_data["schedule"]
    hall=new_hall
    
    movies_db, movie_id = add_movie_to_database(
        movies_db,
        title,
        hall,
        category,
        classification, 
        schedule
    )
    
    print(f"\n✅ Película creada exitosamente: '{title}'")
    print(f"🎭 Categoría: {categories[category]}")
    print(f"🔞 Clasificación: {classifications[classification]}")
    print(f"📅 Fecha: {schedule}")
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


def handle_edit_movie_selection(movies_db: MoviesDatabase) -> tuple[MoviesDatabase, bool] | None:
    """Maneja el submenú de selección de películas para edición."""
    while True:
        clear_screen()
        display_movie_selection_menu(movies_db)
        
        movies_count = get_movies_count(movies_db)
        choice = get_movie_selection_choice(movies_count)
        
        if choice == 9: return None 
            
        movie_ids = get_all_movie_ids(movies_db)

        if 1 <= choice <= len(movie_ids):
            movie_index = choice - 1
            movie_id = movie_ids[movie_index]
            clear_screen()
            movies_db = handle_movie_management(movies_db, movie_id)
            return movies_db, True
        
def edit_classifications():
    classifications, err = read_json(CLASSIFICATION_PATH)
    if err:
        print(f"⚠️ Error al leer el archivo: {err}")
        return

    while True:
        print("\n=== CLASIFICACIONES ACTUALES ===")
        for key, value in classifications.items():
            print(f"{key}. {value}")

        print("\nOpciones:")
        print("1. Agregar nueva clasificación")
        print("2. Modificar una clasificación existente")
        print("3. Eliminar una clasificación")
        print("9. Salir")

        choice = input("Seleccione una opción: ").strip()

        if choice == "1":
            new_key = str(max(map(int, classifications.keys())) + 1)
            new_value = input("Ingrese el texto de la nueva clasificación: ").strip()
            classifications[new_key] = new_value
            print(f"Clasificación agregada con ID {new_key}")

        elif choice == "2":
            edit_key = input("Ingrese el número de la clasificación a modificar: ").strip()
            if edit_key in classifications:
                new_value = input(f"Ingrese el nuevo texto para '{classifications[edit_key]}': ").strip()
                classifications[edit_key] = new_value
                print("Clasificación modificada con éxito.")
            else:
                print("ID no válido.")

        elif choice == "3":
            del_key = input("Ingrese el número de la clasificación a eliminar: ").strip()
            if del_key in classifications:
                del classifications[del_key]
                print(" Clasificación eliminada.")
            else:
                print("ID no válido.")

        elif choice == "9":
            break
        else:
            print("Opción inválida.")

    save_json(classifications, CLASSIFICATION_PATH)
    
def edit_category():
    categories, err = read_json(CATEGORY_PATH)
    if err:
        print(f"⚠️ Error al leer el archivo: {err}")
        return

    while True:
        print("\n=== CATEGORIAS ACTUALES ===")
        for key, value in categories.items():
            print(f"{key}. {value}")

        print("\nOpciones:")
        print("1. Agregar nueva categorias")
        print("2. Modificar una categorias existente")
        print("3. Eliminar una categorias")
        print("9. Salir")

        choice = input("Seleccione una opción: ").strip()

        if choice == "1":
            new_key = str(max(map(int, categories.keys())) + 1)
            new_value = input("Ingrese el texto de la nueva categorias: ").strip()
            categories[new_key] = new_value
            print(f"categorias agregada con ID {new_key}")

        elif choice == "2":
            edit_key = input("Ingrese el número de la categorias a modificar: ").strip()
            if edit_key in categories:
                new_value = input(f"Ingrese el nuevo texto para '{categories[edit_key]}': ").strip()
                categories[edit_key] = new_value
                print("categorias modificada con éxito.")
            else:
                print("ID no válido.")

        elif choice == "3":
            del_key = input("Ingrese el número de la categoria a eliminar: ").strip()
            if del_key in categories:
                del categories[del_key]
                print(" categorias eliminada.")
            else:
                print("ID no válido.")

        elif choice == "9":
            break
        else:
            print("Opción inválida.")

    save_json(categories, CATEGORY_PATH)