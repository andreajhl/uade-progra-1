

from custom_types import MoviesDatabase
from interface.execution.user_flow import run_user_interface


def user_interface(movies_db: MoviesDatabase) -> MoviesDatabase:
    """Punto de entrada para interfaz de usuario."""
    return run_user_interface(movies_db)
