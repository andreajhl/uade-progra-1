from interface.init_interface import init_interface
from interface.admin_interface import admin_interface
from interface.user_interface import user_interface


def handle_exception(e: Exception) -> None:
    """Manejo de excepciones (Keyboard interrupt, TypeErrr, ValueError,Error inesperado)"""
    match e:
        case KeyboardInterrupt():
            print("\nInterrupción del usuario.")
        case TypeError():
            print("Tipo de dato inválido")
        case ValueError():
            print("Valor de dato inválido")
        case _:
            print(f"Ocurrió un error inesperado: {e}")


def main():
    try:
        hall, film_name = init_interface()
        all_halls = [hall]
        all_films = [film_name]

        while True:
            all_halls, all_films, option = admin_interface(all_halls, all_films)

            if option == 1:
                while True:
                    result = user_interface(all_halls, all_films)
                    if isinstance(result, tuple) and len(result) == 2:
                        all_halls, salir_usuario = result
                        if salir_usuario:
                            break
                    else:
                        all_halls = result
                        break
            elif option == 10:
                break
            else:
                print("Opción no reconocida.")
    except Exception as e:
        handle_exception(e)


if __name__ == "__main__":
    main()
