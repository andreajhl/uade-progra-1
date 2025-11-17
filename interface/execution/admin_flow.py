from constants.index import (
    MOVIE_PATH,
    CATEGORY_PATH,
    CLASSIFICATION_PATH,
)
from custom_types import MoviesDatabase
from tools.display.index import clear_screen
from tools.movies.index import (
    get_movies_count,
    add_movie_to_database,
    get_all_movie_ids,
    get_movie_by_id,
)
from interface.ui.display import (
    display_admin_menu_header,
    display_admin_menu_options,
    display_movies_overview,
    display_movie_selection_menu,
)
from interface.ui.input import (
    get_admin_menu_choice_movies,
    get_complete_movie_data,
    get_movie_selection_choice,
)
from tools.json.index import save_json, read_json
from tools.logs.index import read_logs
from tools.movies.index import get_categories, get_classifications
from tools.input.index import custom_input
from tools.logs.index import write_log


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
            result = edit_classifications()
            if result is not None:
                data_changed = True
            continue

        elif admin_choice == 4:
            result = edit_category()
            if result is not None:
                data_changed = True
            continue

        elif admin_choice == 5:
            show_admin_logs()
            continue

        elif admin_choice == 9:
            break

    if data_changed:
        save_json(movies_db, MOVIE_PATH)

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

    categories = get_categories()
    classifications = get_classifications()
    title = movie_data["title"]
    category = movie_data["category"]
    classification = movie_data["classification"]
    schedule = movie_data["schedule"]
    hall = new_hall

    movies_db, movie_id = add_movie_to_database(
        movies_db, title, hall, category, classification, schedule
    )

    print(f"\n✅ Película creada exitosamente: '{title}'")
    print(f"🎭 Categoría: {categories[category]}")
    print(f"🔞 Clasificación: {classifications[classification]}")
    print(f"📅 Fecha: {schedule}")
    print(f"🆔 ID: {movie_id}")

    input("\n📌 Presione Enter para continuar...")
    clear_screen()
    write_log(f"Se creo la pelicula {title}")
    return movies_db


def handle_movie_management(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """Maneja edición de película específica."""
    movie = get_movie_by_id(movies_db, movie_id)
    if not movie:
        print(f"❌ Película con ID {movie_id} no encontrada")
        return movies_db

    from interface.execution.hall_admin_flow import run_hall_admin_interface

    return run_hall_admin_interface(movies_db, movie_id)


def handle_edit_movie_selection(
    movies_db: MoviesDatabase,
) -> tuple[MoviesDatabase, bool] | None:
    """Maneja el submenú de selección de películas para edición."""
    while True:
        clear_screen()
        display_movie_selection_menu(movies_db)

        movies_count = get_movies_count(movies_db)
        choice = get_movie_selection_choice(movies_count)

        if choice == 9:
            return None

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

        valid_options = [1, 2, 3, 9]

        choice = custom_input(
            "Elija una opción: ",
            int,
            error_message="Opción inválida.",
            validator=lambda option: (
                ("Opción inválida.", None)
                if option not in valid_options
                else (None, option)
            ),
        )

        if choice == 1:
            new_key = str(max(map(int, classifications.keys())) + 1)
            new_value = custom_input(
                f"Ingrese el texto de la nueva clasificación: ",
                str,
                validator=lambda classification: (
                    ("El nombre de la nueva clasificación no puede estar vacío.", None)
                    if not classification.strip()
                    else (None, classification.strip())
                ),
            )

            classifications[new_key] = new_value
            print(f"Clasificación agregada con ID {new_key}")
            write_log(f"Se creo la clasificacion {classifications[new_key]}")

        elif choice == 2:
            edit_key = custom_input(
                f"Ingrese el número de la clasificación a modificar: ",
                str,
                validator=lambda classification: (
                    ("El nombre de la clasificación no puede estar vacío.", None)
                    if not classification.strip()
                    else (None, classification.strip())
                ),
            )

            if edit_key in classifications:
                old_classification = classifications[edit_key]

                new_value = custom_input(
                    f"Ingrese el nuevo texto para '{classifications[edit_key]}': ",
                    str,
                    validator=lambda classification: (
                        ("El nombre de la clasificación no puede estar vacío.", None)
                        if not classification.strip()
                        else (None, classification.strip())
                    ),
                )
                classifications[edit_key] = new_value
                print("Clasificación modificada con éxito.")
                write_log(
                    f"Se modifico la clasificacion {old_classification} por {classifications[edit_key]}"
                )
            else:
                print("ID no válido.")

        elif choice == 3:
            del_key = custom_input(
                f"Ingrese el número de la clasificación a eliminar: ",
                int,
                validator=lambda classification: (
                    (None, str(classification))
                    if str(classification) in classifications
                    else ("ID no válido.", None)
                ),
            )

            if del_key in classifications:
                write_log(f"Se elimino la clasificacion {classifications[del_key]}")
                del classifications[del_key]
                print(" Clasificación eliminada.")

        elif choice == 9:
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

        valid_options = [1, 2, 3, 9]

        choice = custom_input(
            "Elija una opción: ",
            int,
            error_message="Opción inválida.",
            validator=lambda option: (
                ("Opción inválida.", None)
                if option not in valid_options
                else (None, option)
            ),
        )

        if choice == 1:
            new_key = str(max(map(int, categories.keys())) + 1)

            new_value = custom_input(
                f"Ingrese el texto de la nueva categorias: ",
                str,
                validator=lambda category: (
                    ("El nombre de la nueva categoria no puede estar vacío.", None)
                    if not category.strip()
                    else (None, category.strip())
                ),
            )

            categories[new_key] = new_value

            print(f"categorias agregada con ID {new_key}")
            write_log(f"Se agrego la clasificacion {categories[new_key]}")

        elif choice == 2:
            edit_key = input("Ingrese el número de la categorias a modificar: ").strip()
            if edit_key in categories:
                old_category = categories[edit_key]

                new_value = custom_input(
                    f"Ingrese el número de la categorias a modificar: ",
                    int,
                    error_message="Opción inválida.",
                    validator=lambda option: (
                        ("Opción inválida.", None)
                        if option not in valid_options
                        else (None, option)
                    ),
                )

                categories[edit_key] = new_value
                write_log(
                    f"Se modifico la clasificacion {old_category} por {categories[edit_key]}"
                )
                print("categorias modificada con éxito.")
            else:
                print("ID no válido.")

        elif choice == 3:
            del_key = custom_input(
                f"Ingrese el número de la categoria a eliminar: ",
                int,
                validator=lambda option: (
                    ("Opción inválida.", None)
                    if option not in valid_options
                    else (None, option)
                ),
            )

            if del_key in categories:
                write_log(f"Se elimino la clasificacion {categories[del_key]}")
                del categories[del_key]
                print(" categorias eliminada.")

        elif choice == 9:
            break
        else:
            print("Opción inválida.")

    save_json(categories, CATEGORY_PATH)


def show_admin_logs():
    """Return admin logs list"""
    return read_logs()
