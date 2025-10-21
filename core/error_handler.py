"""
Error handling for the cinema application.
Provides different error handling strategies for development and deployment modes.
"""

from tools.display.index import clear_screen


def handle_keyboard_interrupt() -> bool:
    """
    Handles KeyboardInterrupt (Ctrl+C) in deployment mode.
    Returns True if user wants to shut down, False to continue.
    """
    clear_screen()
    print("\nInterrupción del usuario.")
    print("Volver a apretar ctrl + c para finalizar.")
    user_choice = input("9 para salir, cualquier cosa para reiniciar: ")
    return user_choice == "9"


def handle_type_error() -> None:
    """Handles TypeError exceptions."""
    clear_screen()
    print("Tipo de dato inválido")


def handle_value_error() -> None:
    """Handles ValueError exceptions."""
    clear_screen()
    print("Valor de dato inválido")


def handle_generic_error(error: Exception) -> None:
    """Handles any other unexpected exceptions."""
    clear_screen()
    print(f"Ocurrió un error inesperado: {error}")


def show_restart_message() -> None:
    """Shows restart message and waits for user input."""
    print("El programa se reiniciará.")
    input("Enter para continuar")


def handle_application_error(error: Exception) -> bool:
    """
    Central error handling dispatcher.
    Returns True if application should shut down, False to continue.
    """
    if isinstance(error, KeyboardInterrupt):
        return handle_keyboard_interrupt()
    elif isinstance(error, TypeError):
        handle_type_error()
    elif isinstance(error, ValueError):
        handle_value_error()
    else:
        handle_generic_error(error)
    
    return False  # Continue running by default