import os
from custom_types import CinemaHall
from tools.view.index import numbers_into_letters, calculate_width
from interface.view.index import show_columns, show_rows

def show_columns(total_columns: int, width_row: int):
    print("Columns", end=" ")
    for c in range(total_columns):
        print(f"{numbers_into_letters(c):>{width_row + 5}}", end="")
    print()
    
def show_rows(hall: CinemaHall, width_seat: int, width_row: int):
    rows = len(hall)
    columns = len(hall[0])

    for f in range(rows):
        print(f"Fila-{f+1:>{width_row}}:", end="  ")
        for c in range(columns):
            print(f"{hall[f][c]:>{width_seat + 2}}", end=" ")
        print()
    
def show_hall(hall: CinemaHall):
    if not hall or not hall[0]:
        print("Sala de Cine (sin butacas)")
        return

    width_seat, width_row, width_total = calculate_width(hall)

    print("Sala de Cine".center(width_total))
    show_columns(len(hall[0]), width_row)
    show_rows(hall, width_seat, width_row)

def clear_screen():
    # Para sistemas Windows
    if os.name == "nt":
        _ = os.system("cls")
    # Para sistemas Unix (Linux, macOS)
    else:
        _ = os.system("clear")