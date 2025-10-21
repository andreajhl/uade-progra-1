"""
User interface entry point - refactored to use MoviesDatabase.
This file now delegates to the execution layer using the new dictionary-based structure.
"""

from custom_types import MoviesDatabase
from interface.execution.user_flow import run_user_interface


def user_interface(movies_db: MoviesDatabase) -> MoviesDatabase:
    """
    Entry point for user interface.
    Delegates to execution layer for clean separation of concerns.
    Uses MoviesDatabase instead of separate lists.
    """
    return run_user_interface(movies_db)
