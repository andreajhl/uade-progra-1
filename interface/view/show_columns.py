import string
from tools.view.numbers_into_letters import numbers_into_letters


def show_columns(total_columns: int, width_row: int):
    print("Columns", end=" ")
    for c in range(total_columns):
        print(f"{numbers_into_letters(c):>{width_row + 5}}", end="")
    print()
