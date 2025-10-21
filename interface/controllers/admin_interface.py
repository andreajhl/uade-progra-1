"""
Admin interface entry point - refactored to use MoviesDatabase.
This file now delegates to the execution layer using the new dictionary-based structure.
"""

from custom_types import MoviesDatabase
from interface.execution.admin_flow import run_admin_interface


def admin_interface(movies_db: MoviesDatabase) -> MoviesDatabase:
    """
    Entry point for admin interface.
    Delegates to execution layer for clean separation of concerns.
    Uses MoviesDatabase instead of separate lists.
    """
    return run_admin_interface(movies_db)
