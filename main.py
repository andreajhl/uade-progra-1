import sys
from time import sleep

from interface.init_interface import init_interface
from interface.admin_interface import admin_interface
from interface.user_interface import user_interface
from interface.view.index import clear_screen

def main():
    hall, film_name = init_interface()
    all_halls = [hall]
    all_films = [film_name]

    while True:
        all_halls, all_films, option = admin_interface(all_halls, all_films)

        if option == -1:
            while True:
                result = user_interface(all_halls, all_films)
                if isinstance(result, tuple) and len(result) == 2:
                    input("Nunca entra aca o si????")
                    all_halls, salir_usuario = result
                    if salir_usuario:
                        break
                else:
                    all_halls = result
                    break
        elif option == -9:
            break
        else:
            print("Opción no reconocida.")

if __name__ == "__main__":

    if sys.argv[-1] == "deploy":
        shut_down = False
        print("modo deploy")
        sleep(2)
        while not shut_down:
            try:
                main()

            except KeyboardInterrupt:
                clear_screen()
                print("\nInterrupción del usuario.")
                print("Volver a apretar cotl + c para finalizar.")
                shut_down = True if input("9 para salir, cualquier cosa para reinicial:") == "9" else False
            
            except TypeError:
                clear_screen()
                print("Tipo de dato inválido")

            except ValueError:
                clear_screen()
                print("Valor de dato inválido")

            except Exception as e:
                clear_screen()
                print(f"Ocurrió un error inesperado: {e}")
                print(f"Ocurrió un error inesperado: {e}")

            finally:
                if not shut_down:
                    print("El programa se reiniciara.")
                    input("Enter para continuar")
    else:
        # Si quisieramos controlar los posibles errores en modo desarrollo
        # seria fundamental usar la libreria estandar traceback para mostrar mas informacion sobre el error
        # la linea y el archivo donde sucedio.
        main()
