

from custom_types import MoviesDatabase
from interface.execution.admin_flow import run_admin_interface


def admin_interface(movies_db: MoviesDatabase) -> MoviesDatabase:
    """Punto de entrada para interfaz de administrador."""

    return run_admin_interface(movies_db)
