"""
View utilities for displaying cinema halls and managing screen.
Contains display functions and screen management utilities.
"""

import os
from custom_types import CinemaHall
from tools.view.index import numbers_into_letters, calculate_width


def _show_columns(total_columns: int, width_row: int) -> None:
    """
    Internal function to show column headers.
    Private function used only within show_hall().
    """
    print("Columns", end=" ")
    for c in range(total_columns):
        print(f"{numbers_into_letters(c):>{width_row + 5}}", end="")
    print()


def _show_rows(hall: CinemaHall, width_seat: int, width_row: int) -> None:
    """
    Internal function to show hall rows with seats.
    Private function used only within show_hall().
    """
    rows = len(hall)
    columns = len(hall[0])

    for f in range(rows):
        print(f"Fila-{f+1:>{width_row}}:", end="  ")
        for c in range(columns):
            print(f"{hall[f][c]:>{width_seat + 2}}", end=" ")
        print()


def clear_screen() -> None:
    """Clears the console screen."""
    # Para sistemas Windows
    if os.name == "nt":
        _ = os.system("cls")
    # Para sistemas Unix (Linux, macOS)
    else:
        _ = os.system("clear")


def show_hall(hall: CinemaHall) -> None:
    """
    Displays the cinema hall layout on screen.
    
    Args:
        hall: Cinema hall structure to display
    """
    if not hall or not hall[0]:
        print("Sala de Cine (sin butacas)")
        return

    width_seat, width_row, width_total = calculate_width(hall)

    print("Sala de Cine".center(width_total))
    _show_columns(len(hall[0]), width_row)
    _show_rows(hall, width_seat, width_row)
